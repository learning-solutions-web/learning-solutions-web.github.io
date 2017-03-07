module.exports = function(grunt) {

  grunt.initConfig({
    less: {
      development: {
        options: {
          compress: true,
          optimization: 2,
          paths: ['css']
        },
        files: {
          'css/main.css': 'less/main.less'
        }
      }
    }
  });

  grunt.registerTask('default', 'less')
  grunt.loadNpmTasks('grunt-contrib-less');
};
