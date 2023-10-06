var contenidoMenuResultado = document.querySelector("#navbarID");

contenidoMenuResultado.innerHTML += `<nav class="navbar navbar-expand-md navbar-dark bg-dark">
<div class="container-fluid">
  <!--icono-->
  <a class="navbar-brand" href="Index.html">
     <img src="imagenes/horizontal_yellow_logo.png" class="img-fluid" style="max-width: 200px; height: auto;">
    
  </a>
  <button
    class="navbar-toggler"
    type="button"
    data-bs-toggle="collapse"
    data-bs-target="#menu"
    aria-controls="navbarSupportedContent"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="menu">
    <ul class="navbar-nav" style="margin-left: 50px;">
      <li class="nav-item">
        <a class="nav-link active" href="Index.html">Inicio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" href="Index.html">Lista de usuarios</a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" href="Index.html">Lista de productos</a>
      </li>
    </ul>
  </div>
</div>
</nav>`;


