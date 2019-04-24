function EliminarProducto(id){
  swal({
            title: '¿Estas seguro que deseas eliminar este Artí´culos?',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, eliminar'
          }).then((result) => {
            if (result.value) {
                $.ajax({
                  url: 'http://localhost:8000/Producto/Productos/Eliminar',
                  method: 'GET',
                  data:{
                    'id_Producto':id
                  },
                  dataType: 'json',
                  success: function (response) {
                    if(response == 200){
                      swal(
                        'Eliminado',
                        'Tu Producto ha sido eliminado',
                        'success'
                      )
                     window.location ="http://localhost:8000/Producto/Productos/Lista";
                    setTimeout ("redirection()", 10000); //tiempo en milisegundos
                    }
                  },
                  error:function() {
                    console.log('error');
                  },
                });
              
            }
          })

 

  
}