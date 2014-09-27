var gulp = require('gulp'),
    less = require('gulp-less');

var less_paths = [
	['frontend/static/css/*.less', 'frontend/static/css']
];
 
gulp.task('less', function() {
	for (var i = 0; i < less_paths.length; i++) {
		gulp.src(less_paths[i][0])
			.pipe(less())
			.pipe(gulp.dest(less_paths[i][1]));
	}
});

gulp.task('watch', function () {
	for (var i = 0; i < less_paths.length; i++) {
   		gulp.watch(less_paths[i][0], ['less']);
	}
});
