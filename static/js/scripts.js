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

modalDelete();
modalUpdate();
