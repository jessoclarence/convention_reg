var Church = function() {
		this.id = null;

		this.name = "";
}

var Churches = function() {
		this.churches = [];
}

Churches.prototype.initialize = function() {
		this.get_all();
}

Churches.prototype.process_all_response = function(json) {
		tmp_arr = [];

		for(i=0; i<json.length; i++) {
				church = new Church();
				church.id = json[i].id;
				church.name = json[i].name;

				tmp_arr.push(church);
		}
		return tmp_arr;
}

Churches.prototype.get_all = function() {
		churches = this;

		$.ajax({
				url: "/regmain/churches/",
				type: "GET",
				dataType: "json"
		}).done(function(json) {
				this.churches = churches.process_all_response(json)
		})
}
