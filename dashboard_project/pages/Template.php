<?php
/**
 * Created by IntelliJ IDEA.
 * User: Alvin
 * Date: 2015-04-29
 * Time: 12:45 PM
 */
?>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Live In Edmonton Admin Dashboard</title>
    <link rel="shortcut icon" href="../dist/images/favicon.ico"/>
    <!-- Bootstrap Core CSS -->
    <link href="../bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="../bower_components/metisMenu/dist/metisMenu.min.css" rel="stylesheet">

    <!-- DataTables CSS -->
    <link href="../bower_components/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.css"
          rel="stylesheet">

    <!-- DataTables Responsive CSS -->
    <link href="../bower_components/datatables-responsive/css/dataTables.responsive.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../dist/css/sb-admin-2.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="../bower_components/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">

    <!-- jQuery -->
    <script src="../bower_components/jquery/dist/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="../bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>


    <![endif]-->
    <!-- jQuery -->
    <script src="../bower_components/jquery/dist/jquery.min.js"></script>


    <!--http://bootsnipp.com/snippets/featured/checked-list-group-->
    <style>
        .state-icon {
            left: -5px;
        }

        .list-group-item-primary {
            color: rgb(255, 255, 255);
            background-color: rgb(66, 139, 202);
        }

        /* DEMO ONLY - REMOVES UNWANTED MARGIN */
        .well .list-group {
            margin-bottom: 0px;
        }

        .modal-row {
            padding: 10px;
            max-width: 350px;
        }

        .modal .modal-body {
            max-height: 580px;
            overflow-y: auto;
            overflow-x: hidden;
        }
    </style>


</head>

<br/>

<div id="wrapper">
    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-fixed-top" role="navigation"
         style="margin-bottom: 0 background-color: rgb(202,86,72);">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Live In Edmonton Admin Dashboard</a>
            </div>
            <!-- /.navbar-header -->

            <ul class="nav navbar-nav navbar-right">

                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                        <i class="fa fa-user fa-fw"></i> <i class="fa fa-caret-down"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-user">
                        <li><a href="#" id="mainInformation"><i class="fa fa-user fa-fw"></i>Account</a>
                        </li>
                        <li><a href="#"><i class="fa fa-gear fa-fw"></i>Setting</a>
                        </li>
                        <li class="divider"></li>
                        <li><a href="#" id="mainLogout"><i
                                    class="fa fa-sign-out fa-fw"></i>logout</a>
                        </li>
                    </ul>
                    <!-- /.dropdown-user -->
                </li>
            </ul>

            <!-- /.navbar-top-links -->
            <!-- /.dropdown -->
            <!-- /.navbar-top-links -->
        </div>
        <div class="navbar-default sidebar" role="navigation" style="margin-top:5px">
            <div class="sidebar-nav navbar-collapse" style="margin-top:0px">
                <ul class="nav" id="side-menu">
                    <li>
                        <a href="#"><i class="fa fa-th-list fa-fw"></i>Service Management</span></a>
                    </li>

                    <li>
                        <a href="#"><i class="fa fa-search fa-fw"></i> Data Analysis</span></a>
                    </li>
                </ul>
            </div>
            <!-- /.sidebar-collapse -->
        </div>
        <!-- /.navbar-static-side -->
        <!--</div>-->
    </nav>

    <!-- Bootstrap Core JavaScript -->
    <script src="../bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="../bower_components/metisMenu/dist/metisMenu.min.js"></script>

    <!-- DataTables JavaScript -->
    <script
        src="../bower_components/datatables/media/js/jquery.dataTables.min.js"></script>
    <script
        src="../bower_components/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.min.js"></script>

    <script src="../../../Source/DataTable-Plugins/api/fnProcessingIndicator.js"></script>

    <!-- Custom Theme JavaScript -->
    <script src="../dist/js/sb-admin-2.js"></script>
    <script>




        $(document).ready(function () {
            $.ajaxSetup({cache:false});
            $(document).on("click", "#mainLogout", function () {
                // jump to login page
               // self.location = '../../../../Report/Shared/login.html';
            });


    </script>

