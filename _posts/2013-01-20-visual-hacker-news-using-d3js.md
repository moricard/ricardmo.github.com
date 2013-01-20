---
layout: post
title: Visual Hacker News
tags: javascript d3js visualisation hackernews jsonp
---

In an attempt to make the web more attractive and lively, I created an interactive visual
representation of the posts displayed on the [Hacker News](http://news.ycombinator.com) website.
I hope this demonstrates that [d3.js](http://d3js.org) can be used to much more extent than just displaying statistics.

## [See it in action](/vishna)
You can see it in action [here](/vishna). Complete source-code is available [on github](https://github.com/ricardmo/vishna).


## [Context](#context)
I have always been fascinated by graphic representation of data. I have had some fun with Mathematica creating
some nice physics animations or visual mathematical proofs but it is hard to share the outcome of the animation
in a format such as mathematica notebooks. Sure, I could always export a video file and post it on youtube or the
like but then you loose all possibility for interactivity.

<aside>Even though Internet Explorer does not follow standards.</aside>
Whether I like it or not, *everybody* has a web browser
and with the rise of javascript, it was a no-brainer to start learning the language seriously if I wanted people to
see and use my work.

In the process of learning the language, I stumbled on a very nice javascript library: [d3.js](http://d3js.org).
While going through the documentation, I realized that all of the examples and tutorials were based on static csv or json files.

As I understand it, D3js is much more than just a bar-charts-and-graphs library and wanted to show some dynamic usage of it
using real life dynamic data that I consult every day. I read the posts on [Hacker News](http://news.ycombinator.com) every day,
why not display them in a fun, visual way.

## [Difficulties](#difficulties)

I had a hard time getting the API to work directly from the javascript. Turns out that to do such a thing, one needs
to use JSONP in order to enable *cross domain json queries*. The regular d3js JSON api does not provide JSONP requests
so I had to use JQuery's `.getJSON` function to get it to work.

<aside markdown='1'> Note that in order for `.getJSON` to launch a JSONP request, the url *must* to end with `&callback=?`. Otherwise, </aside>
{% highlight javascript %}
var urls = {      //API urls
        news  : "http://hndroidapi.appspot.com/news/format/json/page/?appid=vishna&callback=?",
        ask   : "http://hndroidapi.appspot.com/ask/format/json/page/?appid=vishna&callback=?",
        newest: "http://hndroidapi.appspot.com/newest/format/json/page/?appid=vishna&callback=?",
        best  : "http://hndroidapi.appspot.com/best/format/json/page/?appid=vishna&callback=?"
    };

function load( url, callback ){
        $.getJSON(url, function( data ) {
            //bind data to objects
        });
}
{% endhighlight %}
