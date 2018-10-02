var gulp        = require('gulp');
var browserSync = require('browser-sync').create();


gulp.task('default', function() { 
       var files = [   
            '**/*.py',  
            '**/*.html',  
             '**/*.css',   
              '**/*.js'    
            ];
        browserSync.init(files,{
            proxy: "localhost:8000" 
             });
            });


