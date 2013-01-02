import numpy as np
from numpy import sqrt

def onehot(y, size):
    """Retourne l'encodage one-hot d'un entier representant une classe y parmi size
    """
    tmp = np.zeros(size)
    tmp[y] = 1
    return tmp

def onehot_batch(y_array, size):
    """Retourne une matrice d'encodage one-hot
    """
    tmp = list()
    for i in range(y_array.shape[0]):
        tmp.append(onehot(y_array[i]))
    return np.asarray(tmp)

class artificial_neural_net:

    def __init__(self, n_input, n_hidden, n_output, n_batch):
        """Initialise un reseau de neurones artificiel.

        n_input  -- Nombre de neurones d'entree
        n_hidden -- Nombre de neurones sur la couche cachee
        n_output -- Nombre de neurones a la sortie
        n_batch  -- Nombre d'exemples traites par batch.

        """
        self.n_input = n_input
        self.n_hidden = n_hidden
        self.n_output = n_output

        # Initialisation des poids
        self.W1 = np.random.uniform(-sqrt(n_input), sqrt(n_input), (n_hidden, n_input))
        self.b1 = np.zeros(n_hidden)

        self.W2 = np.random.uniform(-sqrt(n_hidden), sqrt(n_hidden), (n_output, n_hidden))
        self.b2 = np.zeros(n_output)

        # Initialisation des vecteur d'activation
        self.ha = np.zeros((n_batch, n_hidden))
        self.hs = np.zeros((n_batch, n_hidden))
        self.oa = np.zeros((n_batch, n_output))
        self.os = np.zeros((n_batch, n_output))

        # Initialisation des gradients
        self.grad_oa = np.zeros((n_batch, self.n_output))
        self.grad_b2 = self.grad_oa
        self.grad_W2 = np.zeros((n_batch, self.W2.shape[0], self.W2.shape[1]))
        self.grad_hs = np.zeros((n_batch, self.n_hidden))
        self.grad_ha = np.zeros((n_batch, self.n_hidden))
        self.grad_b1 = self.grad_ha
        self.grad_W1 = np.zeros((n_batch, self.W1.shape[0], self.W1.shape[1]))
        self.grad_norm = 0

        # Initialisation de la perte et des hyper parametres
        self.loss = np.zeros((n_batch, self.n_output))
        self.risk = 0
        self.reg_term = 0.1

    def fprop(self, values):
        """Effectue la propagation avant dans le reseau.
        """
        self.ha = np.inner(self.W1, values) + self.b1.transpose()
        self.hs = np.tanh(self.ha)
        self.oa = np.inner(self.W2, self.hs) + self.b2
        expoa = np.nan_to_num(np.exp(self.oa))
        self.os = expoa * 1.0 / np.sum(expoa)
        self.loss = np.nan_to_num(-np.log(self.os))
        return self.os

    def bprop(self, values, target):
        """Effectue la propagation arriere dans le reseau.
        """
        self.grad_oa = self.os - onehot_batch(target, self.n_output)
        self.grad_b2 = self.grad_oa
        self.grad_W2 = np.outer(self.grad_oa, np.transpose(self.hs))
        self.grad_hs = np.inner(np.transpose(self.W2), self.grad_oa)
        self.grad_ha = (np.ones(self.grad_hs.shape) - self.hs ** 2) * self.grad_hs
        self.grad_b1 = self.grad_ha
        self.grad_W1 = np.outer(self.grad_ha, np.transpose(values))
        self.grad_norm = np.linalg.norm(self.grad_W1) + np.linalg.norm(self.grad_b1) + np.linalg.norm(self.grad_W2) + np.linalg.norm(self.grad_b2)
        pass

    def finite_difference_verification(self, values, target):
        """Effectue la verification du gradient par difference finie.
        """
        epsilon = 10e-5

        #On calcule la perte pour cet exemple
        self.fprop(values)
        current_loss = self.loss

        #On effectue la difference finie pour chaque element de b1
        for i in range(self.b1.shape[0]):
            self.b1[i] = self.b1[i] + epsilon
            self.fprop(values)
            self.b1[i] = self.b1[i] - epsilon
            estimated_grad = (self.loss[target] - current_loss[target]) / epsilon

            self.bprop(values, target)
            ratio = self.grad_b1[i] / estimated_grad
            print '[info]: gradient ratio %5f for b1[%d]' % (ratio, i)

        #On effectue la difference finie pour chaque element de W1
        for i in range(self.W1.shape[0]):
            for j in range(self.W1.shape[1]):
                self.W1[i][j] += epsilon
                self.fprop(values)
                self.W1[i][j] -= epsilon
                estimated_grad = (self.loss[target] - current_loss[target]) / epsilon

                self.bprop(values, target)
                ratio = self.grad_W1[i][j] / estimated_grad
                print '[info]: gradient ratio %5f for W1[%d][%d]' % (ratio, i, j)

        #On effectue la difference finie pour chaque element de b2
        for i in range(self.b2.shape[0]):
            self.b2[i] = self.b2[i] + epsilon
            self.fprop(values)
            self.b2[i] = self.b2[i] - epsilon
            estimated_grad = (self.loss[target] - current_loss[target]) / epsilon

            self.bprop(values, target)
            ratio = self.grad_b2[i] / estimated_grad
            print '[info]: gradient ratio %5f for b2[%d]' % (ratio, i)

        #On effectue la difference finie pour chaque element de W2
        for i in range(self.W2.shape[0]):
            for j in range(self.W2.shape[1]):
                self.W2[i][j] += epsilon
                self.fprop(values)
                self.W2[i][j] -= epsilon
                estimated_grad = (self.loss[target] - current_loss[target]) / epsilon

                self.bprop(values, target)
                ratio = self.grad_W2[i][j] / estimated_grad
                print '[info]: gradient ratio %5f for W2[%d][%d]' % (ratio, i, j)
        pass

    def finite_difference_verification_batch(self, values, targets):
        """Effectue la verification par difference finie pour un ensemble de valeurs.

        values  -- ensemble de valeurs
        targets -- ensemble des cibles correspondant aux valeurs

        """
        if values.shape[0] != targets.shape[0]:
            print '[error]: Values and targets size does not correspond'
            return

        for i in range(targets.shape[0]):
            print '[info]: Verifing gradient with finite difference for example', i
            self.finite_difference_verification(values[i], targets[i])


    def train(self, train_data, train_labels, learning_rate, normal_factor, n_epoch, batch_size = 1):
        """Entraine le reseau de neurones sur l'ensemble d'entrainement

        train_data    -- Ensemble d'entrainement
        train_labels  -- Cibles correspondant aux examples
        batch_size    -- Taille du lot
        learning_rate -- facteur d'apprentissage
        normal_factor -- facteur de normalisation
        n_epoch       -- nombre de passages sur les batch.

        """
        for epoch in range(n_epoch):
            for i in range(train_data.shape[0] / batch_size):
                self.fprop(train_data[i:(i + 1) * batch_size,:])
                self.bprop(train_data[i:(i + 1) * batch_size,:], train_labels[i:(i + 1) * batch_size])

                #Maintenant que les gradients sont calcules, nous mettons a jour les parametres
                normal_term = normal_factor * ( np.linalg.norm(self.W1) ** 2 + np.linalg.norm(self.W2) ** 2)
                self.W1 -= learning_rate * np.sum(self.grad_W1, axis=0)
                self.b1 -= learning_rate * np.sum(self.grad_b1, axis=0)
                self.W2 -= learning_rate * np.sum(self.grad_W2, axis=0)
                self.b2 -= learning_rate * np.sum(self.grad_b2, axis=0)

                #Nous calculons le nouveau risque
                cost = np.sum(self.loss)

            #print '[info]: Cost of %5f after iteration [%d] of epoch [%d]' % (cost, i, epoch)
            #print '[info]: Gradient of %5f' % (self.grad_norm)

    def compute_predictions(self, test_data):
        """ Calcule les predictions a partir des fonctions apprises
        """
        results = list()
        for i in range(test_data.shape[0]):
            results.append(self.fprop(test_data[i]))
        return np.asarray(results)
