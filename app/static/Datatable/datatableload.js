




$(document).ready( function () {
    $('#tabla_pacientes').DataTable(
      {
      "language": {
                  "lengthMenu": "Mostrar _MENU_ pacientes por página",
                  "zeroRecords": "No se ha encontrado nada - disculpe",
                  "info": "Mostrando página _PAGE_ de _PAGES_",
                  "infoEmpty": "No hay datos disponibles",
                  "infoFiltered": "(filtrado de _MAX_ pacientes disponibles)",
                  "search": "Buscar:",
                  "paginate": {
                        "previous": "anterior",
                        "next": "siguiente"
                      }
              }}

                             );
} );



$(document).ready( function () {
    $('#tabla_mediciones').DataTable(
      {
      "aaSorting": [],
      "language": {
                  "lengthMenu": "Mostrar _MENU_ mediciones por página",
                  "zeroRecords": "No se ha encontrado nada - disculpe",
                  "info": "Mostrando página _PAGE_ de _PAGES_",
                  "infoEmpty": "No hay datos disponibles",
                  "infoFiltered": "(filtrado de _MAX_ mediciones disponibles)",
                  "search": "Buscar:",
                  "paginate": {
                        "previous": "anterior",
                        "next": "siguiente"
                      }
              }}

                             );
} );

$(document).ready( function () {
    $('#tabla_dietas').DataTable(
      {
      "aaSorting": [],
      "language": {
                  "lengthMenu": "Mostrar _MENU_ dietas por página",
                  "zeroRecords": "No se ha encontrado nada - disculpe",
                  "info": "Mostrando página _PAGE_ de _PAGES_",
                  "infoEmpty": "No hay datos disponibles",
                  "infoFiltered": "(filtrado de _MAX_ dietas disponibles)",
                  "search": "Buscar:",
                  "paginate": {
                        "previous": "anterior",
                        "next": "siguiente"
                      }
              }}

                             );
} );


$(document).ready( function () {
    $('#tabla_platos').DataTable(
      {
      "aaSorting": [],
      "pageLength": 50,
      "language": {
                  "lengthMenu": "Mostrar _MENU_ platos por página",
                  "zeroRecords": "No se ha encontrado nada - disculpe",
                  "info": "Mostrando página _PAGE_ de _PAGES_",
                  "infoEmpty": "No hay datos disponibles",
                  "infoFiltered": "(filtrado de _MAX_ platos disponibles)",
                  "search": "Buscar:",
                  "paginate": {
                        "previous": "anterior",
                        "next": "siguiente"
                      }
              }}

                             );
} );


$(document).ready( function () {
    $('#tabla_representaciones').DataTable(
      {
      "aaSorting": [],
      "language": {
                  "lengthMenu": "Mostrar _MENU_ representaciones por página",
                  "zeroRecords": "No se ha encontrado nada - disculpe",
                  "info": "Mostrando página _PAGE_ de _PAGES_",
                  "infoEmpty": "No hay datos disponibles",
                  "infoFiltered": "(filtrado de _MAX_ representaciones disponibles)",
                  "search": "Buscar:",
                  "paginate": {
                        "previous": "anterior",
                        "next": "siguiente"
                      }
              }}

                             );
} );