console.log('Loaded reception_scripts.js')

async function get_daily_checkins() {
	const request = new Request('http://localhost:5000/get_all_reservations_starting_today');
	fetch(request)
		.then(response => response.json())
		.then(reservations => {
			reservation_list = reservations['reservations'];
			let content = ''
			for(let reservation of reservation_list){
			    content += "<div class='card card_container'> <b><p> Reservation ID: " +
			     reservation.reservation_id + "</p></b> <b><p> Client ID: " +
			     reservation.client_id + "</p></b> <b><p> Room Number: " +
			     reservation.room_number + "</p></b> <b><p> Start Date: " +
			     reservation.start_date + "</p></b> <b><p> End Date: " +
			     reservation.end_date + "</p></b> </div>"
			}

			document.getElementById('daily_checkins_content').innerHTML = content;

		}).catch(error => console.warn(error));
}

async function get_daily_checkouts() {
	const request = new Request('http://localhost:5000/get_all_reservations_ending_today');
	fetch(request)
		.then(response => response.json())
		.then(reservations => {
			reservation_list = reservations['reservations'];
			let content = ''
			for(let reservation of reservation_list){
			    content += "<div class='card card_container'> <b><p> Reservation ID: " +
			     reservation.reservation_id + "</p></b> <b><p> Client ID: " +
			     reservation.client_id + "</p></b> <b><p> Room Number: " +
			     reservation.room_number + "</p></b> <b><p> Start Date: " +
			     reservation.start_date + "</p></b> <b><p> End Date: " +
			     reservation.end_date + "</p></b> </div>"
			}

			document.getElementById('daily_checkouts_content').innerHTML = content;

		}).catch(error => console.warn(error));
}


async function add_client(client_id, first_name, last_name, email){

    let client_data = {
            'client_id': client_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            }
    console.log(client_data)
    $.ajax({
      type: "POST",
      contentType: "application/json; charset=utf-8",
      url: "http://localhost:5000/add_client",
      data: JSON.stringify(client_data),
      success: function () {
        alert('Client added successfully');
      },
      dataType: "json"
    });
}


async function add_reservation(client_id, room_number, start_date, end_date){

    let reservation_data = {
            'client_id': client_id,
            'room_number': room_number,
            'start_date': start_date,
            'end_date': end_date,
            }
    console.log(reservation_data)
    $.ajax({
      type: "POST",
      contentType: "application/json; charset=utf-8",
      url: "http://localhost:5000/add_reservation",
      data: JSON.stringify(reservation_data),
      success: function () {
        alert('Reservation added successfully');
      },
      dataType: "json"
    });
}