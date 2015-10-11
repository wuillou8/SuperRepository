var request     = require('request');
var cheerio     = require('cheerio');
var json2csv = require('json2csv');
var fs = require('fs');
var async = require('async');
var csvFields = ['name', 'product_type', 'price'];



// Default user agent, to mimic a real browser..
var userAgent = {
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'
};



var scrape = function(url, done) {
	var requestOptions = {
		url:  url,
		headers: userAgent
	};


	request.get(requestOptions, function(err, httpResponse, body) {
	    if (err) return done(err);
	    var $ = cheerio.load(body);
	    done(err, $);
	})
}

// all products links
var get_all_products = function(done){
	
	var get_all_products_links = [];

	scrape('http://www.yoox.com/UK/shoponline?dept=clothingwomen&gender=D&attributes=%7B%27ctgr%27%3A%5B%27vsttcrmn%27%5D%7D&season=E', function(err, $){
		console.log(err)	
		$('.itemImg').each(function(a,b){
			get_all_products_links.push($(b).find('a').attr('href'));
		})
		done(err, get_all_products_links);
	})	
}


var get_product_details = function(url, cb){
	scrape('http://www.yoox.com' + url, function(err, $){

		var product = {
			name: $('#itemTitle').find('h2').find('a').find('span').html(),
			product_type: $('#itemTitle').find('h1').find('a').find('span').html(),
			price: $('#itemPrice').find('div').find('span').html()
		}
		cb(err, product)
	})
}


var save_csv = function (values){
	json2csv({ data: values, fields: csvFields, nested: true }, function(err, csv) {
	  if (err) console.log(err);
	  fs.writeFile('file.csv', csv, function(err) {
	    if (err) throw err;
	    console.log('file saved');
	  });
	});
}
get_all_products(function(err, all_products_links){
	
	console.log(all_products_links);

	async.mapSeries(all_products_links, get_product_details, function(err, results){
    	// results is now an array of stats for each file
    	console.log(err, results);
    	save_csv(results);
	});

	
})
