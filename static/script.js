function updateSubjects() {
    var year = document.getElementById('year').value;
    var semester = document.getElementById('semester').value;
    
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_subjects/' + year + '/' + semester, true);
    xhr.onload = function() {
        if (this.status === 200) {
            var subjects = JSON.parse(this.responseText);
            var subjectSelect = document.getElementById('subject_name');
            subjectSelect.innerHTML = '';
            subjects.forEach(function(subject) {
                var option = document.createElement('option');
                option.value = subject[0];
                option.textContent = subject[0];
                subjectSelect.appendChild(option);
            });
        }
    };
    xhr.send();
}
