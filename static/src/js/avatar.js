// Получаем ссылку на элементы
const avatarImage = document.getElementById('avatar-image');
const avatarUpload = document.getElementById('avatar-upload');

// Добавляем обработчик события click на аватар
avatarImage.addEventListener('click', () => {
  avatarUpload.click();
});
