// Create a function to select elements
const selectElement = (element) => {
	document.querySelector(element);
};

// Open and close nav on click
selectElement('.menu-icons').addEventListener('click', () => {
	selectedElement('nav').classList.toggle('active');
});
