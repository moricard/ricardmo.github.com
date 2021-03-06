---
layout: post
title: The making of this blog
---

So here we are, it is the first day of the year 2013 and as a good resolution, I decided to start contributing in the open source community. I thought the first step in doing so was to create a blog and start sharing.



This blog <s>is running</s> will be running on a raspberry pi in my living room and I tought as a first post, I could try and document the making of this setup.

### [The Plan](#the_plan)

I have this raspberry pi hanging around and tought it was a shame to have unused computer power in the house. I might as well use it for something useful. Why not run this blog on it? It has enough power to handle the modest network traffic this blog is going to generate.

I am aiming for something simple here, just a plain personal logging system. I tought about ready-made solutions like blogger and wordpress but I wanted to make something from scratch, something I would have control over from beginning to end.

Earlier this week, I read [this post](http://blog.alexbrowne.info/how-i-made-my-blog-faster/) and it led me to adopt [Jekyll](http://jekyllrb.com/) as the ultimate solution. It is very simple and elegant, it can parse [markdown](http://daringfireball.net/projects/markdown/), which I happen to like. It also uses [Pygments](http://pygments.org) when rendering it's [Liquid](http://liquidmarkup.org) templates, which makes sharing code a breeze. But still, nothing superfluous, just a clean and lean web framework that generates a static web site that we are going to serve with a standard HTTP server.

### [The System](#the_system)

I am not going to go through the whole process of setting up a raspberry pi, it is pretty [straightforward](http://elinux.org/RPi_Easy_SD_Card_Setup) and the documentation is thorough. The only SD card I had available was a 1Gb µSD card I took from an old cell phone so I had to use a shrinked down version of [Raspbian Wheezy](http://www.raspberrypi.org/downloads).

The first thing we will need is a working web server on the pi. As root, in the terminal, we install a pre-built version of [nginx](http://nginx.org), a high performance HTTP server.
{% highlight bash %}
root@raspberrypi$ apt-get install nginx
{% endhighlight %}

Et voilà, we now have a working HTTP server serving static files located in `/usr/share/nginx/www/`. Default configuration worked out-of-the-box for me but any tuning should be done in the configuration files situated in `/etc/nginx/`.

### [Setting up Jekyll](#setting_up_jekyll)

From Mac OS X, installing Jekyll was as simple as:
{% highlight bash %}
% gem install jekyll
{% endhighlight %}
You will find [detailed instructions](https://github.com/mojombo/jekyll/wiki/Install) for your system.

We then need to create the file structure for the blog.
{% highlight bash %}
% mkdir blog
% cd !$
% mkdir _includes _layouts _posts _site css images
% touch _config.yml
{% endhighlight %}

The next step is not necessary as Jekyll defaults to usable configuration if this file is not valid, but hey, let's do things thoroughly. Note that the `server` and `auto` lines are there only for front-end development, `_config.yml`:
{% highlight yaml %}
{% include config.yml %}
{% endhighlight %}

We also need to create our template layouts. Create and edit the file: `_layouts/default.html`.
{% highlight html %}
{% include default1.html %}
{% endhighlight %}

Now, for our posts: `_layouts/post.html`
{% highlight html %}
{% include post1.html %}
{% endhighlight %}

We can now create the frontpage like so: `/index.html`
{% highlight html %}
{% include index1.html %}
{% endhighlight %}

And we are ready for a first post. The way Jekyll works is that it will render all files situated in `_posts/` with a format corresponding to `YYYY-MM-DD-TITLE.markdown`. These files have to begin with some [YAML front-matter](https://github.com/mojombo/jekyll/wiki/YAML-Front-Matter). Here is an example: `_posts/2012-12-31-beginning.markdown`

{% highlight yaml %}
{% include samplepost.md %}
{% endhighlight %}

### [The Deployment](#the_deployment)

To deploy on the raspberry pi, since we are already running a web server serving static files on `/usr/share/nginx/www/`, all we have to do is build the site with Jekyll and sync it to the pi. A simple one-liner does just this:
{% highlight bash %}
% jekyll --no-server && rsync -avz --delete _site/ root@raspberrypi.local:/usr/share/nginx/www/
{% endhighlight %}

That's it, we now have a working blog. It's pretty ugly really, so next time I will guide you through the design of this blog. [Part II here](/2013/01/02/designing-this-blog/)
