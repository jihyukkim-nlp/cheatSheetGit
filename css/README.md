# CSS

ref
- https://www.w3schools.com/css/
- https://developer.mozilla.org/ko/docs/Web/CSS

## Basics
> 크롬 화면에서 [좌클릭 - Inspect - Styles] 에서 CSS 속성을 동적으로 바꾸고 HTML 이 어떻게 보여지는지 실시간으로 확인 할 수 있다.
### Loading into html file
~~~html
<link rel="stylesheet" type="text/css" href="css/master.css">
~~~
### Syntax
~~~css
selected tag{
	property: value;
}
~~~
### Color
> Color Picker: https://www.google.com/search?q=color+picker&oq=color+picker&aqs=chrome..69i57j69i60j0l4.2409j0j7&sourceid=chrome&ie=UTF-8

``` rgb, rgba, #001122(hexacode)```

### Selector
> ref: https://www.w3schools.com/cssref/css_selectors.asp
~~~css
.intro{} /* Selects all elements with class="intro" */
#firstname{} /* Selects the element with id="firstname" */ 
*{} /* Selects all elements */ 
p{} /* Selects all <p> elements */
div, p{} /* Selects all <div> elements and all <p> elements */
div p{} /* Selects all <p> elements inside <div> elements */
div > p{} /* Selects all <p> elements where the parent is a <div> element */
div + p{} /* Selects all <p> elements that are placed immediately after <div> elements */
p ~ ul{} /* Selects every <ul> element that are preceded by a <p> element */
~~~

### Specificity
> html 파일에는 하나의 태그에 class 와 id 가 동시에 올 수 있으며 여러 개의 class 가 할당될 수도 있다.
~~~html
<div class="class1" id="id1" class="class2">
	Some contents
</div>
~~~
동일한 Attribute 에 대해 서로 다른 Value 가 존재한다면 어떤 Value 를 실제로 적용?
> ref) https://designshack.net/articles/css/what-the-heck-is-css-specificity/

## Fonts and Texts
~~~css
.font_test{
	font-family: "Arial"; /* Note that not every font-family is ported by every OS */
	font-size: 10px;
	font-style: italic;
	font-weight: bold;
	text-align: center;
}
~~~
> font-family 와 OS 
> * https://www.cssfontstack.com/
> 
> embed font from cdn
> * https://fonts.google.com/
> * https://fontlibrary.org/
> 
> font-size
> * relative to body font-size (default body font-size is 16px)
> * 1em=16px (default font-size) , 2em=32px, etc 

## Box Model
![Box Model Image](https://cdn-images-1.medium.com/max/565/1*6DrszcyPybYDGziiS9CWdg.png)
~~~css
div{
	border: 4px solid blue;
	width: 25%;
	text-align: center;
	margin:10px 20px 100px 400px; /* top, right, bottom, left */
	/* margin: auto */ /* align to center */
	padding: 200px;
}
~~~

# Bootstrap
> Get from CDN
> https://getbootstrap.com/docs/4.2/getting-started/download/
~~~html
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
~~~
> Examples
> https://getbootstrap.com/docs/4.2/examples/

> Themes
> https://themes.getbootstrap.com/

> Components
> https://getbootstrap.com/docs/4.2/components/alerts/
> 예) Buttons, Forms, Jumbotron, Input group, Navbar

> Utilities
> https://getbootstrap.com/docs/4.2/utilities/borders/

> Layout (Grid)
> https://getbootstrap.com/docs/4.2/layout/overview/

> 대부분의 bootstrap 을 활용한 tag 들은 container class (predefined) 안에 넣는다.
~~~html
<div class="container"> ... inner tags ... </div>
~~~
