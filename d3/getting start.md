~~~
$ python3 -m http.server >> resolve CORF constraint
~~~
### svg, rectangle, circle, ellipse, path, line, text
~~~
<svg width="400" height="600">
  <rect x="0" y="0" width="50" height="50" fill="green" stroke="grey" stroke-width="5px"></rect>
  <circle cx="90" cy="25" r="5" fill="black"></circle>
  <ellipse cx="145" cy="50" rx="15" ry="30" fill="blue"></ellipse>
  <line x1="185" y1="5" x2="230" y2="40" stroke="red" stroke-width="5"></line>
  <text x="260" y="25" font-size="20px" fill="orange" text-anchor="middle"> Hellow World</text>
  <text x="260" y="25" font-size="20px" fill="orange" text-anchor="end"> Hellow World</text>
  <text x="260" y="25" font-size="20px" fill="orange" text-anchor="start"> Hellow World</text>
  <path ></path>
</svg>
~~~

### select, append, attr
~~~
d3.select("[tag|.class|#id]");
d3.selectAll("[tag|.class|#id]");
[object].append("[figure tag|svg tag]");
[svg object|figure object].attr("[attribute]", "[value]");
~~~

### method chaining
~~~
var rect= d3.select("#canvas")
            .append("rect")
            .attr("x",25)
            .attr("y",0)
            .attr("width", 150)
            .attr("height", 60)
            .attr("fill", "green")
~~~
