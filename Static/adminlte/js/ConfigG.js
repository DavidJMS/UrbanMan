//Tipos de EGRESOS
function NuevoTipoDeEgreso() {
 swal({
  html: '<h2>Añadir Tipo de Egreso</h2><h4 style="color:blue">Ingrese el tipo de Egreso que desea registrar</h4>',
  input: 'text',
  inputPlaceholder: 'Tipo De Egreso',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/configuracion/Tipo/De/Egreso/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'TipoDeEgreso':value,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Felicidades!',
					      'Agregamos Su Tipo de Egreso satisfactoriamente.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else if (status == 401) {
		    		
		    		swal(
					      'Error!',
					      'Ya posees un tipo de Egreso con ese nombre .',
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su tipo de Egreso!", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
    }
  }
})



}


function  EditarTipoEgreso(id) {
	        $.ajax({
		    
		    url : 'http://localhost:8000/configuracion/Tipo/De/Egreso/Get/Registro/',
		  	method: 'GET',
		    data : { 
		    	'id':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(Datajson) {
		    	if (Datajson) {
			    	swal({
					  html: '<h1>Editar Tipo de Egreso</h1><h3 style="color:grey">'+	Datajson.Datajson +'</h3>',
					  input: 'text',
					  inputPlaceholder: ''+Datajson.Datajson+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    
					    url : 'http://localhost:8000/configuracion/Tipo/De/Egreso/Update/Registro/',
					    
					    data : { 
					    	'id_tipo_de_egreso':id,
					    	'nameTypeEgreso':value,
					    },
					    
					    dataType : 'json',
					    
					    success : function(status) {
					    	//console.log(status)
					    	if (status == 200) {
					    		//todo correcto 
					    		swal(
								      'Felicidades!',
								      'Agregamos Su tipo de Egreso satisfactoriamente.',
								      'success'
								    );
					        	location.href ="/configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees un tipo con ese nombre .',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su petición!", "error")
					    	}
					    },
					 
					    
					    error : function(xhr, status) {
					        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
					    },
					 
					    
					});
			    }
			  }
			})
		   }
		    },
		 		 
		});
           }
function EliminarTipoEgreso(id) {
	console.log("hey")
swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este tipo de Egreso?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Eliminarlo!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		
           	$.ajax({
		    
		    url : '/configuracion/Tipo/De/Egreso/Solicitud/Eliminar/Registro/',
		   
		    data : { 
		    	'id_Tipo_Egreso':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(status) {
		    	if (status == 200) {
		    		 
		    		swal(
					      'Borrado!',
					      'Hemos Borrado satisfactoriamente tu petición.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar !", "error")
		    	}
		    },
		 
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    
		});
           }
        });
}

//Tipos de INGRESOS
function NuevoTipoDeIngreso(){
	swal({
  html: '<h2>Añadir Tipo de Ingreso</h2><h4 style="color:blue">Ingrese el tipo de Ingreso que desea registrar</h4>',
  input: 'text',
  inputPlaceholder: 'Tipo De Ingreso',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/configuracion/Tipo/De/Ingreso/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'TipoDeIngreso':value,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Felicidades!',
					      'Agregamos Su Tipo de Ingreso satisfactoriamente.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else if (status == 401) {
		    		
		    		swal(
					      'Error!',
					      'Ya posees un tipo de Ingreso con ese nombre .',
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su tipo de Ingreso!", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
    }
  }
})
}


function EditarTipoIngreso(id){
	$.ajax({
		    
		    url : 'http://localhost:8000/configuracion/Tipo/De/Ingreso/Get/Registro/',
		  	method: 'GET',
		    data : { 
		    	'id':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(Datajson) {
		    	if (Datajson) {
			    	swal({
					  html: '<h1>Editar Tipo de Ingreso</h1><h3 style="color:grey">'+	Datajson.Datajson +'</h3>',
					  input: 'text',
					  inputPlaceholder: ''+Datajson.Datajson+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    
					    url : 'http://localhost:8000/configuracion/Tipo/De/Ingreso/Update/Registro/',
					    
					    data : { 
					    	'id_tipo_de_ingreso':id,
					    	'nameTypeIngreso':value,
					    },
					    
					    dataType : 'json',
					    
					    success : function(status) {
					    	//console.log(status)
					    	if (status == 200) {
					    		//todo correcto 
					    		swal(
								      'Felicidades!',
								      'Agregamos Su tipo de Ingreso satisfactoriamente.',
								      'success'
								    );
					        	location.href ="/configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees un tipo con ese nombre .',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su petición!", "error")
					    	}
					    },
					 
					    
					    error : function(xhr, status) {
					        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
					    },
					 
					    
					});
			    }
			  }
			})
		   }
		    },
		 		 
		});
}

function EliminarTipoIngreso(id) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este tipo de Ingreso?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Eliminarlo!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		
           	$.ajax({
		    
		    url : '/configuracion/Tipo/De/Ingreso/Solicitud/Eliminar/Registro/',
		   
		    data : { 
		    	'id_Tipo_Ingreso':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(status) {
		    	if (status == 200) {
		    		 
		    		swal(
					      'Borrado!',
					      'Hemos Borrado satisfactoriamente tu petición.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar !", "error")
		    	}
		    },
		 
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    
		});
           }
        });
}
//TIPOS EMPLEADOS
function NuevoTipoDeEmpleado(){
	swal({
  html: '<h2>Añadir Tipo de Empleado</h2><h4 style="color:blue">Ingrese el tipo de Empleado que desea registrar</h4>',
  input: 'text',
  inputPlaceholder: 'Tipo De Empleado',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/configuracion/Tipo/De/Empleado/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'TipoDeEmpleado':value,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Felicidades!',
					      'Agregamos Su Tipo de Empleado satisfactoriamente.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else if (status == 401) {
		    		
		    		swal(
					      'Error!',
					      'Ya posees un tipo de Empleado con ese nombre .',
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su tipo de Empleado!", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
    }
  }
})
}

function EditarTipoEmpleado(id) {
	$.ajax({
		    
		    url : 'http://localhost:8000/configuracion/Tipo/De/Empleado/Get/Registro/',
		  	method: 'GET',
		    data : { 
		    	'id':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(Datajson) {
		    	if (Datajson) {
			    	swal({
					  html: '<h1>Editar Tipo de Empleado</h1><h3 style="color:grey">'+	Datajson.Datajson +'</h3>',
					  input: 'text',
					  inputPlaceholder: ''+Datajson.Datajson+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    
					    url : 'http://localhost:8000/configuracion/Tipo/De/Empleado/Update/Registro/',
					    
					    data : { 
					    	'id_tipo_de_empleado':id,
					    	'nameTypeEmpleado':value,
					    },
					    
					    dataType : 'json',
					    
					    success : function(status) {
					    	//console.log(status)
					    	if (status == 200) {
					    		//todo correcto 
					    		swal(
								      'Felicidades!',
								      'Agregamos Su tipo de Empleado satisfactoriamente.',
								      'success'
								    );
					        	location.href ="/configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees un tipo con ese nombre .',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su petición!", "error")
					    	}
					    },
					 
					    
					    error : function(xhr, status) {
					        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
					    },
					 
					    
					});
			    }
			  }
			})
		   }
		    },
		 		 
		});
}

function EliminarTipoEmpleado(id) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este tipo de Empleado?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Eliminarlo!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		
           	$.ajax({
		    
		    url : '/configuracion/Tipo/De/Empleado/Solicitud/Eliminar/Registro/',
		   
		    data : { 
		    	'id_tipo_de_empleado':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(status) {
		    	if (status == 200) {
		    		 
		    		swal(
					      'Borrado!',
					      'Hemos Borrado satisfactoriamente tu petición.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar !", "error")
		    	}
		    },
		 
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    
		});
           }
        });
}

//PROVEEDORES
function NuevoTipoDeProveedor(){
	swal({
  html: '<h2>Añadir Tipo de Proveedor</h2><h4 style="color:blue">Ingrese el tipo de Proveedor que desea registrar</h4>',
  input: 'text',
  inputPlaceholder: 'Tipo De Proveedor',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/configuracion/Tipo/De/Proveedor/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'TipoDeProveedor':value,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Felicidades!',
					      'Agregamos Su Tipo de Proveedor satisfactoriamente.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else if (status == 401) {
		    		
		    		swal(
					      'Error!',
					      'Ya posees un tipo de Proveedor con ese nombre .',
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su tipo de Proveedor!", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
    }
  }
})
}

function EditarTipoProveedor(id){
	$.ajax({
		    
		    url : 'http://localhost:8000/configuracion/Tipo/De/Proveedor/Get/Registro/',
		  	method: 'GET',
		    data : { 
		    	'id':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(Datajson) {
		    	if (Datajson) {
			    	swal({
					  html: '<h1>Editar Tipo de Proveedor</h1><h3 style="color:grey">'+	Datajson.Datajson +'</h3>',
					  input: 'text',
					  inputPlaceholder: ''+Datajson.Datajson+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    
					    url : 'http://localhost:8000/configuracion/Tipo/De/Proveedor/Update/Registro/',
					    
					    data : { 
					    	'id_tipo_de_proveedor':id,
					    	'nameTypeProveedor':value,
					    },
					    
					    dataType : 'json',
					    
					    success : function(status) {
					    	//console.log(status)
					    	if (status == 200) {
					    		//todo correcto 
					    		swal(
								      'Felicidades!',
								      'Agregamos Su tipo de Proveedor satisfactoriamente.',
								      'success'
								    );
					        	location.href ="/configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees un tipo con ese nombre .',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su petición!", "error")
					    	}
					    },
					 
					    
					    error : function(xhr, status) {
					        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
					    },
					 
					    
					});
			    }
			  }
			})
		   }
		    },
		 		 
		});
}

function EliminarTipoProveedor(id) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este tipo de Proveedor?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Eliminarlo!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		
           	$.ajax({
		    
		    url : '/configuracion/Tipo/De/Proveedor/Solicitud/Eliminar/Registro/',
		   
		    data : { 
		    	'id_tipo_de_proveedor':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(status) {
		    	if (status == 200) {
		    		 
		    		swal(
					      'Borrado!',
					      'Hemos Borrado satisfactoriamente tu petición.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar !", "error")
		    	}
		    },
		 
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    
		});
           }
        });
}

//CLIENTES
function NuevoTipoDeCliente() {
	swal({
  html: '<h2>Añadir Tipo de Cliente</h2><h4 style="color:blue">Ingrese el tipo de Cliente que desea registrar</h4>',
  input: 'text',
  inputPlaceholder: 'Tipo De Cliente',
  showCancelButton: true,
  inputValidator: (value) => {
  	if (value == '') {
  		return !value && 'Necesitas escribir algo!'
  	}
    else{
    	  	$.ajax({
		    // la URL para la petición
		    url : '/configuracion/Tipo/De/Cliente/Solicitud/Nuevo/Registro/',
		    // la información a enviar
		    // (también es posible utilizar una cadena de datos)
		    data : { 
		    	'TipoDeCliente':value,
		    },
		    // el tipo de información que se espera de respuesta
		    dataType : 'json',
		    // código a ejecutar si la petición es satisfactoria;
		    // la respuesta es pasada como argumento a la función
		    success : function(status) {
		    	if (status == 200) {
		    		//todo correcto 
		    		swal(
					      'Felicidades!',
					      'Agregamos Su Tipo de Cliente satisfactoriamente.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else if (status == 401) {
		    		
		    		swal(
					      'Error!',
					      'Ya posees un tipo de Cliente con ese nombre .',
					      'error'
					    );
		        	
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al cargar su tipo de Cliente!", "error")
		    	}
		    },
		 
		    // código a ejecutar si la petición falla;
		    // son pasados como argumentos a la función
		    // el objeto de la petición en crudo y código de estatus de la petición
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    // código a ejecutar sin importar si la petición falló o n
		});
    }
  }
})
}

function EditarTipoCliente(id){
	$.ajax({
		    
		    url : 'http://localhost:8000/configuracion/Tipo/De/Cliente/Get/Registro/',
		  	method: 'GET',
		    data : { 
		    	'id':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(Datajson) {
		    	if (Datajson) {
			    	swal({
					  html: '<h1>Editar Tipo de Cliente</h1><h3 style="color:grey">'+	Datajson.Datajson +'</h3>',
					  input: 'text',
					  inputPlaceholder: ''+Datajson.Datajson+'',
					  showCancelButton: true,
					  inputValidator: (value) => {
					  	if (value == '') {
					  		return !value && 'Necesitas escribir algo!'
					  	}
					    else{
			    	  	$.ajax({
					    
					    url : 'http://localhost:8000/configuracion/Tipo/De/Cliente/Update/Registro/',
					    
					    data : { 
					    	'id_tipo_de_cliente':id,
					    	'nameTypeCliente':value,
					    },
					    
					    dataType : 'json',
					    
					    success : function(status) {
					    	//console.log(status)
					    	if (status == 200) {
					    		//todo correcto 
					    		swal(
								      'Felicidades!',
								      'Agregamos Su tipo de Cliente satisfactoriamente.',
								      'success'
								    );
					        	location.href ="/configuracion/";
					    	}
					    	else if (status == 401) {
					    		//todo correcto 
					    		swal(
								      'Error!',
								      'Ya posees un tipo con ese nombre .',
								      'error'
								    );
					        	
					    	}
					    	else{
					    		swal("OOOh!", "Hemos tenido un problema al cargar su petición!", "error")
					    	}
					    },
					 
					    
					    error : function(xhr, status) {
					        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
					    },
					 
					    
					});
			    }
			  }
			})
		   }
		    },
		 		 
		});
}

function EliminarTipoCliente(id) {
	swal({
		  title: '¿Estas Seguro?',
		  text: "¿Estas Seguro de que deseas eliminar este tipo de Cliente?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, Quiero Eliminarlo!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		
           	$.ajax({
		    
		    url : '/configuracion/Tipo/De/Cliente/Solicitud/Eliminar/Registro/',
		   
		    data : { 
		    	'id_tipo_de_cliente':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(status) {
		    	if (status == 200) {
		    		 
		    		swal(
					      'Borrado!',
					      'Hemos Borrado satisfactoriamente tu petición.',
					      'success'
					    );
		        	location.href ="/configuracion/";
		    	}
		    	else{
		    		swal("OOOh!", "Hemos tenido un problema al borrar !", "error")
		    	}
		    },
		 
		    error : function(xhr, status) {
		        swal("OOOh!", "Hemos tenido un problema con el Servidor!", "error")
		    },
		 
		    
		});
           }
        });
}