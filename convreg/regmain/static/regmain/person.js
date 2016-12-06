// Person model

var TMPL_PERSON = '' +
		'<div class="row">' +
		'  <div class="row">' +
		'    <div class="col-sm-4">' +
		'      <label>First Name</label>' +
		'    </div>' +
		'    <div class="col-sm-4">' +
		'      <input type="text" name="txt_first_name" ' +
		'             class="txt_first_name" />' +
		'    </div>' +
		'  </div>' +
		'  <div class="row">' +
		'    <div class="col-sm-4">' +
		'      <input type="button" value="Submit" ' +
		'             class="btn_person_submit"/>' +
		'    </div>' +
		'  </div>' +
		'  <div class="church-container"></div>' +
		'</div>'

var Person = function(family_id) {
		this.id = null;

		this.first_name = "";
		this.last_name = "";
		this.dob = null;
		this.sex = null;
		this.church_id = null;
		this.family_id = family_id;
		this.contact_info_id = null;
		this.att_type_id = null;

		this.container = null;
		this.html_node = $(TMPL_PERSON)[0];

		this.txt_first_name = null;
		this.btn_submit = null;
}

Person.prototype.render = function(container) {
		this.container = container;
		container.append(this.html_node);

		this.bind_inputs();
}

Person.prototype.update_values_from_form = function() {
		if (this.container === null) {
				return false;
		}

		this.first_name = this.txt_first_name.value;
		return true;
}

Person.prototype.process_response = function(json) {
		this.first_name = json.first_name;

		this.update_html_fields();
}

Person.prototype.update_html_fields = function() {
		this.txt_first_name.value = this.first_name;
}

Person.prototype.submit = function() {
		if (this.container === null) {
				return false;
		}

		this.update_values_from_form();

		p = this;

		$.ajax({
				url: "/regmain/add_person/",
				data: {
						first_name: this.first_name
				},
				type: "POST",
				dataType: "json"
		}).done(function(json) {
				p.process_response(json);
		});
		return true;
}

Person.prototype.bind_inputs = function() {
		if (this.container === null) {
				return false;
		}

		this.txt_first_name = $(this.html_node).find(
				'input.txt_first_name')[0];
		this.btn_submit = $(this.html_node).find(
				'input.btn_person_submit')[0];

		p = this;
		$(this.btn_submit).on("click", function(){p.submit();});

		return true;
}
