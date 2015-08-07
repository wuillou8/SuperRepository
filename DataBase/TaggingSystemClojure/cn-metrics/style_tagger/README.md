#Tagging Library
This is a tagging library for CN website. The events are stored into the cassandra database.

##Tags function

The tag function is defined on resources/public/style_event.js and has the following fields (expecting hashmaps):

	function send_event(userdata, category, action, eventdata, pagedata);
whereas:

userdata: data about the user (userId, country, ethnic origin, sexual orientation, mother's name, favourite recipe, political stance, ...)	
category: for now, 'browse' or 'transaction',	
action: for instance view, click, menu-navigation (in browse) or place in cart, buy, payment confirmation (transaction),	
eventdata: for a 'browser' category event, a hashmap with for instance a button details. For a 'transaction' event, for instance product and transaction details (id, brand, price, costs).	
pagedata: data about the page viewed, ideally a list of parameters encoding the particular webpage.
##Examples

For now, find examples on resources/public/test.html

As a summary:
window.user = {id: "user1234", country: "france"}	
window.view = {id: "view"}	
window.pagedata = { id: "a std page", param1: "param1 ..." }	
window.click = {id: "click"}	
window.menu = {id: "menu"}	
window.prod1 = { id: "P1", name: "T-Shirt", category: "Clothing", brand: "Google", variant: "black", price: "29.20", costs: "18.75" }	

tags on webpage:

	<button onClick="send_event(window.user, 'browse', 'view', window.view, window.pagedata)">
	or
	<button onClick="send_event(window.user, 'transaction', 'purchase', window.item, window.pagedata)">    

## Run Website & tests
	start cassandra (see below)
	>lein ring server-headless
	>lein figwheel

## Cassandra

	install: >brew install cassandra
	run cassandra: >cassandra 
	access	cassandra: >cqlsh (for instance)