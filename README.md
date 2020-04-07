# InterVolga_Task1
test task 1
index.html:
 
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'proj/style.css' %}">
<div class="banner">
<img src="{% static 'proj/banner.png' %}" alt="Banner"/>
</div>
 
style.css
 
:
img {
width: 200px; max-width: 100px;
}
div {
width: 200px;
height: 100px;
transition: all 2s ease-in-out;
}

div:hover {
transform: scale(2,2)
}
