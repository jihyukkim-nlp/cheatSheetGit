## > <script src="https:d3js.org/d3.v5.js"></script>

### turn on server
> resolve CORF constraint
~~~bash
$ python3 -m http.server
~~~

### svg, rectangle, circle, ellipse, path, line, text
~~~javascript
<svg width="400" height="600">
	<rect x="0" y="0" width="50" height="50" fill="green" stroke="grey" stroke-width="5px"></rect>
		<!--> stroke 는 boarder 를 의미 <--!>
  	
	<circle cx="90" cy="25" r="5" fill="black"></circle>
  	
	<ellipse cx="145" cy="50" rx="15" ry="30" fill="blue"></ellipse>
  	
	<line x1="185" y1="5" x2="230" y2="40" stroke="red" stroke-width="5"></line>
  		<!--> line에서 stroke 는 선(figure) 자체의 굵기를 의미 <--!>
	<text x="260" y="25" font-size="20px" fill="orange" text-anchor="middle"> Hellow World</text>
  	<text x="260" y="25" font-size="20px" fill="orange" text-anchor="end"> Hellow World</text>
  	<text x="260" y="25" font-size="20px" fill="orange" text-anchor="start"> Hellow World</text>
  	
	<path ></path>
</svg>
~~~
> SVG = Scallable Vector Graphics 
<br></br>
> svg canvas 를 벗어나는 도형은 화면에 나타나지 않는다. 

### select, append, attr  
> jQuery 와 유사 
~~~javascript
d3.select("[tag|.class|#id]"); 
d3.selectAll("[tag|.class|#id]");
[object].append("[figure tag|svg tag]");
[svg object|figure object].attr("[attribute]", "[value]");
~~~

### method chaining
~~~javascript
var rect= d3.select("#canvas")
            .append("rect")
            .attr("x",25)
            .attr("y",0)
            .attr("width", 150)
            .attr("height", 60)
            .attr("fill", "green")
~~~

### loading data 
> d3.v5 (version5 rather than 4)
~~~javascript
d3.json("[path/to/.json]").then(function(data){
	// Code goes here
}).catch(function(error){
	console.log(error);
});
~~~


