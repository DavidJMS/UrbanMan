function EliminarCategoria(id){
  swal({
            title: '¿Estas seguro que deseas eliminar esta Categoria?',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, eliminar'
          }).then((result) => {
            if (result.value) {
                $.ajax({
                  url: 'http://localhost:8000/Producto/Categoria/Eliminar',
                  method: 'GET',
                  data:{
                    'id_Categoria':id
                  },
                  dataType: 'json',
                  success: function (response) {
                    if(response == 200){
                      swal(
                        'Eliminado',
                        'Tu Categoria ha sido eliminado',
                        'success'
                      )
                     window.location ="http://localhost:8000/Producto/Categorias/Lista";
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