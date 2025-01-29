/* This validation checks if the files were uploaded by the user */
document.getElementById('submit').addEventListener('click', function(event) {
    // get the files from the page when it's submitted
        let rubricFile = document.getElementById('rubric').files.length;
        let quizFile = document.getElementById('quiz').files.length;

        // grab the error message tag
        let errorMessage = document.getElementById('error-message');  // Get the error message container


        // if the files aren't there, tell the user in the html
        if (rubricFile === 0 || quizFile === 0) {
            event.preventDefault();  
            errorMessage.textContent = 'Rubric and student response CSV files must be included';
        }
});
