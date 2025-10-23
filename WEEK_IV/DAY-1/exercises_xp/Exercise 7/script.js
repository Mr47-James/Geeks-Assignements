// JS file
(function(userName) {
    const navbar = document.getElementById('navbar');
    
    const userDiv = document.createElement('div');
    userDiv.style.display = 'flex';
    userDiv.style.alignItems = 'center';
    userDiv.style.gap = '8px';

    const profileImg = document.createElement('img');
    profileImg.src = 'https://via.placeholder.com/40'; // placeholder profile picture
    profileImg.alt = `${userName}'s profile`;
    profileImg.style.borderRadius = '50%';
    profileImg.style.width = '40px';
    profileImg.style.height = '40px';

    const nameSpan = document.createElement('span');
    nameSpan.textContent = userName;

    userDiv.appendChild(profileImg);
    userDiv.appendChild(nameSpan);
    navbar.appendChild(userDiv);
})("John");
