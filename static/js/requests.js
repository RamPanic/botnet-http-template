
function post_request(url, data, callback) {

	return $.ajax({
	
		'url': url,
        'type': 'POST',
        'contentType': 'application/json',
        'data': JSON.stringify(data),
        'dataType': 'json',
        'success': callback
    
    });

} 

function delete_request(url, callback) {

    return $.ajax({
    
        'url': url,
        'type': 'DELETE',
        'success': callback
    
    });

} 

function get_request(url, callback){

	return $.ajax({

		'url': url,
        'type': 'GET',
        'success': callback
    
    });

}