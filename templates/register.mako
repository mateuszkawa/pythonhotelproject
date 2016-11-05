<%inherit file="layout.mako"/>


            <div class="header header-filter" style="background-image: url('../assets/material/img/city.jpg'); background-size: cover; background-position: top center;">
                <div class="container">
                    <div class="row">
                        <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3">
                            <div class="card card-signup">
                                <form class="form-horizontal" role="form" method="post" action="/hotel/rest/signin">
                                    <div class="header header-primary text-center">
                                        <h4>Sign Up</h4>
                                    </div>
                                    <p class="text-divider">Or Be Classical</p>
                                    <div class="content">

                                        <div class="input-group">
                                            <span class="input-group-addon">
                                                <i class="material-icons">login</i>
                                            </span>
                                            <input type="text" class="form-control" placeholder="First Name...">
                                        </div>

                                        <div class="input-group">
                                            <span class="input-group-addon">
                                                <i class="material-icons">email</i>
                                            </span>
                                            <input type="text" class="form-control" placeholder="Email...">
                                        </div>

                                        <div class="input-group">
                                            <span class="input-group-addon">
                                                <i class="material-icons">password</i>
                                            </span>
                                            <input type="password" placeholder="Password..." class="form-control" />
                                        </div>
                                    </div>
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons">Mako example usage:</i>
                                            ${example_dictionary['example_key_1']}
                                            % for elem in example_dictionary['example_key_2']:
                                                % if elem == 'example_list_val_2':
                                                    <div><span><h4>${elem}</h4></span></div>
                                                % else:
                                                    <div><span><i>${elem}</i></span></div>
                                                % endif
                                            % endfor
                                        </span>
                                    </div>
                                    <div class="footer text-center">
                                        <a href="#" class="btn btn-simple btn-primary btn-lg">Get Started</a>
                                        <button type="submit" class="btn btn-default">Sign In</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
