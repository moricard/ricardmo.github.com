---
layout: post
title: Designing this blog
tags: css html design
---


Simple does not mean boring, let's make something beautiful out of this. I am not a designer but I believe I am creative enough to come up with something original and good looking on my own. Here are the steps that I went through while designing this blog.


## [Scaffolding](#scaffolding)

First thing we need is some kind of structure. I have some experience using [Twitter Bootstrap](http://twitter.github.com/bootstrap/) and even though it's powerful, I didn't need that much of a framework for the frontend.



<aside markdown='1'>
All I really needed was a grid that was responsive to various screen sizes. I found this very simple grid [1140Grid](http://cssgrid.net) that does just that and weights only `2kb`. Here is the scaffolded post template. *Note: the space between two { { is only there so Liquid does not interpret them.*
</aside>

{% highlight html %}
{% include post.html %}
{% endhighlight %}


## [Typography](#typography)

This is a text-oriented blog so this part might be the most important one. There is a [whole science](http://www.alistapart.com/articles/more-meaningful-typography/) behind typography and what makes text beautiful or ugly. I didn't want to get dirty building a type system so I found [Gridlover](http://www.gridlover.net) which is a nice tool to build css rules for a type system.

Fonts give personnality and expressiveness and I wanted to get away from default fonts while keeping a classic and elegant feel to the text. After digging in [Google webfonts](http://www.google.com/webfonts), I settled for [<span style="font-family: 'Cinzel Decorative', cursive;">Cinzel Decorative</span>](http://www.google.com/webfonts/specimen/Cinzel+Decorative) for titles and [Open Sans](http://www.google.com/webfonts/specimen/Open+Sans) for paragraphs.

## [Colors](#colors)

I am colorblind, *not joking*. But still, it seems like 90% of the readable web follows the <span style="background: #fefefe;">almost-white-background/dark-text</span> pattern and that kind of bores me. I didn't want to go <span style="background: #010101;color:#fefefe;">reverse</span>, equally boring. There must be a way to have a colorful website without sacrificing readability.

Most of the screens nowadays are big and there is definitely a trend towards full-screen applications. I tend to find long lines of text quite difficult to read so I am going to limit text to a moderately narrow column in the middle of the page. That being said, I could put a white background for the text and color all around but I think that it breaks the sentiment of purity, elegance and openness given by having the text lying undelimited by borders or color change in the middle of the screen. <em>(I know, very profound)</em> [See for yourself](/alternate-index.html).

Maybe I'm being bold, but even with my colorblindness, I am going for full colors. So I kind of picked up this <span style="background-color: #1bb5e0;">blue color</span> randomly as I found it lively, cheerful, yet mellow and suitable for a background. Also, it should be noted that most of my t-shirts were in that color range back in my teenage years.

I used [Color Scheme Designer](http://colorschemedesigner.com/) to pick highlight and shadow colors (remember, I am colorblind). As a bonus, using a colored background allows for some nice engraved text effect using a simple CSS text-shadow trick which is simply not possible to do on a white background.

{% highlight css %}
body {
    /* engraved text for dark colors */
    text-shadow: 0px 1px 1px #7CD6F0;
}

a {
    /* engraved text for light colors */
    text-shadow: 0px -1px 1px #097392;
}
{% endhighlight %}

## [Code Highlighting](#code_hilighting)

There is going to be a substential amount of code sharing here so I needed to write some css styles that [Pygments](http://pygments.org) recognizes. I was lazy and instead of building them, I borrowed from [@richleland](https://github.com/richleland/pygments-css) and made a couple modifications to the `monokai.css`.

## [Putting it all together](#putting_it_all_together)

The process of developing the frontend was as simple as running jekyll in auto refresh server mode on my local machine and reloading the browser as I was tweaking the `css/style.css` file. In the root of the Jekyll project from the terminal:

{% highlight bash %}
% jekyll --server --auto
{% endhighlight %}

You can see the whole source on the [Github repo](https://github.com/ricardmo/ricardmo.github.com/). For simplicity, I decided to host this blog on Github pages at the moment since I don't have a dynamic dns set up for my initial plan of hosting this on my raspberry pi. It was as simple as creating a Github repository named `ricardmo.github.com`, note that it is important that the name of the repo is `yourusername.github.com` or else pages won't work.
Once the repository is set up, cloning it on my machine and then copying the whole file structure we created in the [previous post](/2013/01/01/the-making-of-this-blog/) in the repo was all I needed to do.

{% highlight bash %}
% git clone git@github.com:ricardmo/ricardmo.github.com.git
% copy -r blog/* ricardmo.github.com
% cd !$
% git add .
% git commit -m "initial commit"
% git push
{% endhighlight %}

And that's it, 10 minutes later we have a free hosted blog.
