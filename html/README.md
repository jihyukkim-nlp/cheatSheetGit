# HTML Basics
ref) https://www.w3schools.com/html/
## 1. List
### 1.1. Ordered List
~~~html
<ol>
	<li> First </li>
	<li> Second </li>
	<li> Third </li>
</ol>
~~~
### 1.2. Unordered List
~~~html
<ul>
	<li>First</li>
	<li>Second</li>
	<li>Third</li>
</ul>
~~~
  
## 2. Table
~~~html
<table>
	<thead> <!-- Column Names -->
		<th>Name</th> 
		<th>Age</th>
		<th>Dept</th>
	</thead>
	<tr> <!-- Column Rows -->
		<td>KimJihyeok</td>
		<td>26</td>
		<td>CS</td>
	</tr>
	<tr> <!-- Column Rows -->
		<td>HongGilDong</td>
		<td>28</td>
		<td>HIS</td>
	</tr>
</table>
~~~

## 3. Form
### 3.0. Basics
~~~html
<form>
	<input type="email" name="useremail" value="abcd@gogo.com">
	<input type="password" name="userpassword" value="">
	<input type="submit" name="" value="Click Me">
	<input type="color" name="" value="Color Information">
	<input type="text" name="description" value="default text">
</form>
~~~
#### 3.0.1. required
	<input type="text" name="me" placeholder="who are you?" required> <!-- neccessary input for submit -->
	<input type="text" name="password" placeholder="password" required> <!-- neccessary input for submit -->
	<input type="text" name="tosay" placeholder="anything to say?"> <!-- not neccessary for submit -->
	<input type="submit" name="submit" value="Click"> <!-- if you click this your url gonna change -->
#### 3.0.2. placeholder
``` <input type="email" name="useremail" placeholder="Enter Email"> ``` <!-- if some text input placeholder disappear -->

### 3.1. Action
~~~html
<form action="https://fb.com" method="get">
	<input type="text" name="" value="go to facebook">
	<input type="submit" name="" value="submit">
</form>
~~~

### 3.2. Label
#### 3.2.1. Basic
	<form>
		<label> Enter: 
			<input type="text" name="" value="First">
		</label>
		<label> Enter: 
			<input type="text" name="" value="Second">
		</label>
	</form>
#### 3.2.2. Using label with for
	<form>
		<label for='id1'> Enter </label>
		<input id="id1" type="text" name="" value="First">
	</form>

### 3.3. Radio Button
#### 3.3.1. input type="radio"
	<form>
		<p> Where are you come from? </p>
		<label for='fromkorea'> From Korea? </label>
		<input id="fromkorea" type="radio" name="" value="">
	</form>
#### 3.3.2. choose one of them
	<!-- Using name attribute in input tag -->
	<!-- give same name to both input tag name attribute -->
	<form>
		<p> Where are you come from? </p>
		<label for='fromkorea'> From Korea? </label>
		<input id="fromkorea" type="radio" name="comefrom" value="">
		<label for='fromothers'> From Other Countries? </label>
		<input id="fromothers" type="radio" name="comefrom" value="">
	</form>

### 3.4. Select
	<form>
		<p> Are you good at English? </p>
		<select name="degree">
			<option value=5>Very Good</option>
			<option value=4>Good</option>
			<option value=3>Normal</option>
			<option value=2>Bad</option>
			<option value=1>Very Bad</option>
		</select>
	</form>

### 3.5. Textarea
	<form>
		<p> Anything to comment? </p>
		<textarea name="comment" rows="8" cols="80"></textarea>
	</form>

### 3.6. Submit
	<form>
		<p> Where are you come from? </p>
		<label for='fromkorea'> From Korea? </label>
		<input id="fromkorea" type="radio" name="comefrom" value="fromkorea">
		<label for='fromothers'> From Other Countries? </label>
		<input id="fromothers" type="radio" name="comefrom" value="fromothers">
	
		<p> Are you good at English? </p>
		<select name="degree">
			<option value=5>Very Good</option>
			<option value=4>Good</option>
			<option value=3>Normal</option>
			<option value=2>Bad</option>
			<option value=1>Very Bad</option>
		</select>

		<p> Anything to comment? </p>
		<textarea name="comment" rows="8" cols="80"></textarea>
		
		<input type="submit" name="" value="SUBMIT">
		<!-- if you click SUBMIT button, your url gonna chane -->
		<!-- original_url/?comefrom=fromothers&degree=3&comment=it+was+great%21 -->
		<!-- name=value [&name=value]* pattern -->
	</form>
