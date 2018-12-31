# HTML Basics
ref) https://www.w3schools.com/html/
## 1. List
### 1.1. Ordered List
  ~~~
  <ol>
		<li> First </li>
		<li> Second </li>
		<li> Third </li>
	</ol>
  ~~~
### 1.2. Unordered List
  ~~~
  <ul>
		<li>First</li>
		<li>Second</li>
		<li>Third</li>
	</ul>
  ~~~
 
## 2. Table
~~~
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
~~~
<form>
	<input type="email" name="useremail" value="abcd@gogo.com">
	<input type="password" name="userpassword" value="">
	<input type="submit" name="" value="Click Me">
	<input type="color" name="" value="Color Information">
	<input type="text" name="description" value="default text">
</form>
~~~
### 3.0. Basics
#### 3.0.1. required
~~~ 
<input type="text" name="me" placeholder="who are you?" required> <!-- neccessary input for submit -->
<input type="text" name="password" placeholder="password" required> <!-- neccessary input for submit -->
<input type="text" name="tosay" placeholder="anything to say?"> <!-- not neccessary for submit -->
<input type="submit" name="submit" value="Click">
~~~
#### 3.0.2. placeholder
``` <input type="email" name="useremail" placeholder="Enter Email"> ``` <!-- if some text input placeholder disappear -->
### 3.1. Action
	<form action="https://fb.com" method="get">
		<input type="text" name="" value="go to facebook">
		<input type="submit" name="" value="submit">
	</form>
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
		<label for='First'> Enter </label>
		<input id="First" type="text" name="" value="First">
	</form>
