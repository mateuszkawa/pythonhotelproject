<%inherit file="layout.mako"/>


            <div class="header header-filter" style="background-image: url('../assets/material/img/city.jpg'); background-size: cover; background-position: top center;">
                <div class="container">
                    <div class="row">
                        <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3">
                            <div class="card card-signup">
                                <form class="form-horizontal" role="form" method="post" action="/hotel/rest/register">
                                    <div class="header header-primary text-center">
                                        <h4>Sign Up</h4>
                                    </div>
                                    <div class="content">
                                            <input id="Email" name="Email" type="text" class="form-control" placeholder="Email..." />
                                            <input id="Password" name="Password" type="password" placeholder="Password..." class="form-control"/>
                                            <input id="FirstName" name="FirstName" type="text" class="form-control" placeholder="First Name..."/>
                                            <input id="LastName" name="LastName" type="text" class="form-control" placeholder="Last Name..."/>
                                            <input id="Phone" name="Phone" type="text" class="form-control" placeholder="Phone..."/>
                                    </div>
                                    <div class="footer text-center">
                                        <a href="#" class="btn btn-simple btn-primary btn-lg">Get Started</a>
                                        <button type="submit" class="btn btn-default">Register</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
