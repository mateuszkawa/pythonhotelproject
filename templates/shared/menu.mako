<nav class="navbar navbar-default">
  <div class="container-fluid">
    <ul class="nav navbar-nav">
      <li class="active"><a href="/main">Home</a></li>
      <li><a href="/rooms">Rooms</a></li>
      % if menu['access_lvl'] < 3:
      <li><a href="/admin">Admin</a></li>
      % endif
    </ul>
    <a class="navbar-brand navbar-right" href="/logout">LogOut</a>
    <a class="navbar-brand navbar-right" href="/rooms/my">MyRooms</a>
  </div>
</nav>