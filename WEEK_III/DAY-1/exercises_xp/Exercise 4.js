// ==========================
// BUILDING OBJECT
// ==========================
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2
    },
    tenants: ["Sarah", "Dan", "David"],
    tenantsInfo: {
        Sarah: { rooms: 3, rent: 1200 },
        Dan: { rooms: 4, rent: 1000 },
        David: { rooms: 1, rent: 1000 }
    }
};

// 1. Number of floors
console.log("Number of floors:", building.numberOfFloors);

// 2. Apartments on floors 1 and 3
console.log("Apartments on floor 1:", building.numberOfAptByFloor.firstFloor);
console.log("Apartments on floor 3:", building.numberOfAptByFloor.thirdFloor);

// 3. Second tenant and number of rooms
const secondTenant = building.tenants[1];
console.log("Second tenant:", secondTenant);
console.log("Number of rooms:", building.tenantsInfo[secondTenant].rooms);

// 4. Check rent and update Dan's rent if needed
const sarahRent = building.tenantsInfo.Sarah.rent;
const davidRent = building.tenantsInfo.David.rent;
const danRent = building.tenantsInfo.Dan.rent;

if (sarahRent + davidRent > danRent) {
    building.tenantsInfo.Dan.rent = 1200;
}

console.log("Dan's updated rent:", building.tenantsInfo.Dan.rent);
