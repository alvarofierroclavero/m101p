<html>
<head>
	<title>Show Collections</title>
</head>
<body>
%if error_val:
	<h3>There was an error</h3>
	<p>Database: {{db_name}}<br />
	Error message: {{error_message}}</p>
%else:
	<h3>Here are the collections in the {{db_name}} database.</h3>
	<ol>
	%for collection in collections:
		<li>{{collection}}</li>
	%end
	</ol>
%end
</body>
</html>