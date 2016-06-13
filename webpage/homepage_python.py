HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
<title>Dyscover</title>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<script >
function showInput(){
    var location = document.getElementById("q_id").value;
    var result = "";
    $("#display").html("Fetching results...");
    $.getJSON("http://localhost:8000/api/search/", {q:location}, function(data, status){
        restaurant_list = data["Restaurants"];
        for (index = 0; index < restaurant_list.length; index++){
            restaurant_name = JSON.stringify(restaurant_list[index]["Name"]);
            restaurant_url = JSON.stringify(restaurant_list[index]["Url"]);
            restaurant_name = restaurant_name.slice(1, -1);
            restaurant_url = restaurant_url.slice(1, -1);
            result += (index + 1) + ". " + "<a href=" + restaurant_url + ">"
                + restaurant_name + "</a>" + "<br />";
        }
        $("#display").html(result);
    })
    .error(function(data, status){
        $("#display").html("Not found");
    });
    return false;
}
</script>
</head>
<body>

<h1>Find a restaurant nearby</h1>
<h3>Enter a location:</h3>

<form id="target" >
    <input type="text" name="q" value="" id="q_id">
    <input type="button" value="Find" onclick="showInput();">
</form>
<br />
<p><span id="display"> </span></p>

</body>
</html>
'''
