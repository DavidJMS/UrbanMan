function Del(id) {
	swal({
		  title: 'Esta usted Seguro?',
		  text: "De que desea eliminar a este empleado?",
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonColor: '#3085d6',
		  cancelButtonColor: '#d33',
		  confirmButtonText: 'Si, deseo eliminarlo!'
		}).then(function (result) {
           if(result.value){
           	var screen = $('#loading-screen');
    		
            $.ajax({
		    
		    url : 'http://localhost:8000/Staff/elim/',
		  	method: 'GET',
		    data : {
		    	'id_employee':id,
		    },
		    
		    dataType : 'json',
		    
		    success : function(status) {
		    	if (status == 200) {
		    		
		    		swal(
					      'Eliminado!',
					      'Este Empleado fue Eliminado Exitosamente',
					      'success'
					    );
		        	location.href ="http://localhost:8000/Staff/staffPrincipal/";
		    	}
		    	else{
		    		swal("mmm..!", "parece que tuvimos un problema", "error")
		    	}
		    },
		 		 
		});
           }
        });
}


