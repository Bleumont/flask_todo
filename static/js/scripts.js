function modalUpdate() {
  $modal = document.querySelector('.modal-update');
  document.addEventListener('click', (e) => {
    if (e.target.matches('.btn-update')) {
      e.stopPropagation();
      $modal.classList.toggle('is-active');
    }
  });
}
function modalDelete() {
  $modal = document.querySelector('.modal-delete');
  $btn = document.querySelector('.btn-delete');
  $btn.addEventListener('click', (e) => {
    $modal.classList.toggle('is-active');
  });
}
function taskDone() {}

function searchFilter() {
  const $inputBox = document.querySelector('#search-box'),
    $searchArea = document.getElementById('notes'),
    $searchItem = $searchArea.getElementsByClassName('note-item');
  let $filter = $inputBox.value.toUpperCase();
  for (let ele of $searchItem) {
    let a = ele.getElementsByTagName('textarea')[0];
    let txtValue = a.value || a.innerText;
    if (txtValue.toUpperCase().indexOf($filter) > -1) {
      ele.style.visibility = 'initial';
      ele.style.opacity = 1;
      ele.style.order = 0;
    } else {
      ele.style.visibility = 'hidden';
      ele.style.opacity = 0;
      ele.style.order = 1;
    }
  }
}
document.addEventListener('keyup', (e) => {
  searchFilter();
});
