var gulp = require('gulp'),
    less = require('gulp-less');
    coffee = require('gulp-coffee');

var less_paths = [
    ['frontend/static/frontend/css/*.less', 'frontend/static/frontend/css'],
];

var coffee_paths = [
    ['frontend/static/frontend/js/*.coffee', 'frontend/static/frontend/js'],
];

gulp.task('less', function() {
	for (var i = 0; i < less_paths.length; i++) {
		gulp.src(less_paths[i][0])
			.pipe(less())
			.pipe(gulp.dest(less_paths[i][1]));
	}
});

gulp.task('coffee', function() {
    for (var i = 0; i < coffee_paths.length; i++) {
        gulp.src(coffee_paths[i][0])
            .pipe(coffee())
            .pipe(gulp.dest(coffee_paths[i][1]));
    }
})

gulp.task('watch', function () {
	for (var i = 0; i < less_paths.length; i++) {
        gulp.watch(less_paths[i][0], ['less']);
	}
    for (var i = 0; i < coffee_paths.length; i++) {
        gulp.watch(coffee_paths[i][0], ['coffee']);
    }
});

gulp.task('default', ['less', 'coffee']);
