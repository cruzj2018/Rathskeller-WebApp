$(document).ready(function () {
	// PAGE ONE START
	new Splide("#splide", {
		type: "loop",
		perPage: 5,
		perMove: 1,
		pagination: false,
		breakpoints: {
			1200: {
				perPage: 4,
			},
			668: {
				perPage: 3,
			},
			500: {
				perPage: 2,
			},
			300: {
				perPage: 1,
			},
		},
	}).mount();

	$.each([1, 1, 1, 1], function (key, value) {
		$("#listData").append(`
                                                                <div
                                    class="
																		col-12
                                        col-lg-6
                                        mt-4
                                    "
                                >
																<div data-bs-toggle="modal" data-bs-target="#exampleModal" class="d-flex align-items-center listCardCont boxCont pointer">
																<div>
																		<img
																				src="https://images.unsplash.com/photo-1513104890138-7c749659a591?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1470&q=80"
																				alt=""
																		/>
																</div>
																<div class="ms-4 py-2">
																		<h6 class="mb-1 mb-0 h5">Barbecue Bacon Chicken</h6>
																		<p class="small mb-0 text-secondary mt-1">
																				Lorem ipsum dolor sit amet consectetur adipisicing
																				elit. Dolore Lorem ipsum dolor sit amet.
																		</p>
																		<div class="d-flex align-items-baseline mt-1">
																				<h6 class="price h4 mb-0 fw-bold"><i class="bi bi-cart3"></i>  $10.00</h6>
																		</div>
																</div>
																</div>
                                </div>
`);
	});

	$.each([1, 1, 1, 1], function (key, value) {
		$("#listData2").append(`
                                                                <div
                                    class="
																		col-12
                                        col-lg-6
                                        mt-4
                                    "
                                >
																<div data-bs-toggle="modal" data-bs-target="#exampleModal2" class="d-flex align-items-center listCardCont boxCont pointer">
																<div>
																		<img
																				src="https://images.pexels.com/photos/3686790/pexels-photo-3686790.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
																				alt=""
																		/>
																</div>
																<div class="ms-4 py-2">
																		<h6 class="mb-1 mb-0 h5">Coco Cola</h6>
																		<p class="small mb-0 text-secondary mt-1">
																				Lorem ipsum dolor sit amet consectetur adipisicing
																				elit. Dolore Lorem ipsum dolor sit amet.
																		</p>
																		<div class="d-flex align-items-baseline mt-1">
																				<h6 class="price h4 mb-0 fw-bold"><i class="bi bi-cart3"></i>  $10.00</h6>
																		</div>
																</div>
																</div>
                                </div>
`);
	});

	$.each([1, 1, 1, 1], function (key, value) {
		$("#listData3").append(`
                                                                <div
                                    class="
																		col-12
                                        col-lg-6
                                        mt-4
                                    "
                                >
																<div data-bs-toggle="modal" data-bs-target="#exampleModal3" class="d-flex align-items-center listCardCont boxCont pointer">
																<div>
																		<img
																				src="https://images.pexels.com/photos/2983098/pexels-photo-2983098.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
																				alt=""
																		/>
																</div>
																<div class="ms-4 py-2">
																		<h6 class="mb-1 mb-0 h5">Cheese Burger</h6>
																		<p class="small mb-0 text-secondary mt-1">
																				Lorem ipsum dolor sit amet consectetur adipisicing
																				elit. Dolore Lorem ipsum dolor sit amet.
																		</p>
																		<div class="d-flex align-items-baseline mt-1">
																				<h6 class="price h4 mb-0 fw-bold"><i class="bi bi-cart3"></i>  $10.00</h6>
																		</div>
																</div>
																</div>
                                </div>
`);
	});
});

// PAGE ONE START
// FOR LISTING SHOW AND HIDE END

// HAMBERGER START GLOBAL
const sidebar = document.getElementById("sideBarId");
document.getElementById("hambergerBtn").addEventListener("click", () => {
	sidebar.style.display = "block";
	sidebar.style.opacity = "1";
	sidebar.style.top = "0%";
	sidebar.style.left = "0%";
	sidebar.style.transform = "none";
});

const closeSidebar = () => {
	sidebar.style.display = "none";
	sidebar.style.opacity = "0";
	sidebar.style.transition = "1s all";
};
// HAMBERGER END GLOBAL

// CATEGORY MENU START
nav1.addEventListener("click", () => {
	nav1.classList.add("active");
	nav2.classList.remove("active");
	nav3.classList.remove("active");
	nav4.classList.remove("active");
	nav5.classList.remove("active");
});

nav2.addEventListener("click", () => {
	nav2.classList.add("active");
	nav1.classList.remove("active");
	nav3.classList.remove("active");
	nav4.classList.remove("active");
	nav5.classList.remove("active");
});

nav3.addEventListener("click", () => {
	nav3.classList.add("active");
	nav1.classList.remove("active");
	nav2.classList.remove("active");
	nav4.classList.remove("active");
	nav5.classList.remove("active");
});

nav4.addEventListener("click", () => {
	nav4.classList.add("active");
	nav1.classList.remove("active");
	nav2.classList.remove("active");
	nav3.classList.remove("active");
	nav5.classList.remove("active");
});

nav5.addEventListener("click", () => {
	nav5.classList.add("active");
	nav1.classList.remove("active");
	nav2.classList.remove("active");
	nav3.classList.remove("active");
	nav4.classList.remove("active");
});

// SIDEBAR CATEGORY MENU START
sNav1.addEventListener("click", () => {
	sNav1.classList.add("active");
	sNav2.classList.remove("active");
	sNav3.classList.remove("active");
	sNav4.classList.remove("active");
	sNav5.classList.remove("active");
	sidebar.style.display = "none";
	sidebar.style.opacity = "0";
	sidebar.style.transition = "1s all";
});

sNav2.addEventListener("click", () => {
	sNav2.classList.add("active");
	sNav1.classList.remove("active");
	sNav3.classList.remove("active");
	sNav4.classList.remove("active");
	sNav5.classList.remove("active");
	sidebar.style.display = "none";
	sidebar.style.opacity = "0";
	sidebar.style.transition = "1s all";
});

sNav3.addEventListener("click", () => {
	sNav3.classList.add("active");
	sNav1.classList.remove("active");
	sNav2.classList.remove("active");
	sNav4.classList.remove("active");
	sNav5.classList.remove("active");
	sidebar.style.display = "none";
	sidebar.style.opacity = "0";
	sidebar.style.transition = "1s all";
});

sNav4.addEventListener("click", () => {
	sNav4.classList.add("active");
	sNav1.classList.remove("active");
	sNav2.classList.remove("active");
	sNav3.classList.remove("active");
	sNav5.classList.remove("active");
	sidebar.style.display = "none";
	sidebar.style.opacity = "0";
	sidebar.style.transition = "1s all";
});

sNav5.addEventListener("click", () => {
	sNav5.classList.add("active");
	sNav1.classList.remove("active");
	sNav2.classList.remove("active");
	sNav3.classList.remove("active");
	sNav4.classList.remove("active");
	sidebar.style.display = "none";
	sidebar.style.opacity = "0";
	sidebar.style.transition = "1s all";
});
// SIDEBAR CATEGORY MENU END
