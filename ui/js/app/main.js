//Load Web App JavaScript Dependencies/Plugins
define([
    "knockout",
    "jquery",
//    "modernizr",
    "underscore",
    "backbone",
    "bootstrap"
], function(ko)
{

    //do stuff
    console.log('required plugins loaded...');
    $('#main').append("<p> Hello World </p>");

    this.firstName = ko.observable('Bert');
    this.firstNameCaps = ko.computed(function() {
            return this.firstName().toUpperCase();
        }, this);
});
