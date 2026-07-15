const year = document.getElementById("year");

if (year) {
  const currentYear = new Date().getFullYear();
  year.textContent = currentYear;
  year.dateTime = String(currentYear);
}
