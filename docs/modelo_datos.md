# Modelo de datos — SIGR (línea base)

En la línea base los datos se gestionan en memoria. El modelo relacional
previsto para la siguiente iteración es el siguiente:

- **usuario**(id, nombre_usuario, clave_hash, rol)
- **plato**(id, nombre, categoria, precio, disponible)
- **pedido**(id, plato_id, estado, hora, mesero_id)
- **reserva**(id, nombre_cliente, fecha, hora, personas)
- **venta**(id, fecha, total, cantidad_pedidos)

Relaciones: un pedido referencia un plato; una venta consolida los pedidos
entregados del día.
