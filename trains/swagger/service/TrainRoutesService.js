'use strict';


/**
 * Add a new train route
 * Add a new train route
 *
 * body TrainRoute Create a new train route
 * returns TrainRoute
 **/
exports.addTrainRoute = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "cost" : 3700,
  "from_city" : "Тверь",
  "to_city" : "Санкт-Петербург",
  "id" : 10,
  "to_time" : "20.08.2024 3:58",
  "from_time" : "19.08.2024 20:24"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Add a new train route
 * Add a new train route
 *
 * body TrainRoute Create a new train route
 * returns TrainRoute
 **/
exports.addTrainRoute = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "cost" : 3700,
  "from_city" : "Тверь",
  "to_city" : "Санкт-Петербург",
  "id" : 10,
  "to_time" : "20.08.2024 3:58",
  "from_time" : "19.08.2024 20:24"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Deletes a train route
 * delete a train route
 *
 * id Long Train route id to delete
 * no response value expected for this operation
 **/
exports.deleteTrainRoute = function(id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Find train route by ID
 * Returns a single train route
 *
 * id Long ID of train route to return
 * returns TrainRoute
 **/
exports.getTrainRouteById = function(id) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "cost" : 3700,
  "from_city" : "Тверь",
  "to_city" : "Санкт-Петербург",
  "id" : 10,
  "to_time" : "20.08.2024 3:58",
  "from_time" : "19.08.2024 20:24"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Get all train routes
 * Get all train routes
 *
 * returns List
 **/
exports.getTrainRoutes = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "cost" : 3700,
  "from_city" : "Тверь",
  "to_city" : "Санкт-Петербург",
  "id" : 10,
  "to_time" : "20.08.2024 3:58",
  "from_time" : "19.08.2024 20:24"
}, {
  "cost" : 3700,
  "from_city" : "Тверь",
  "to_city" : "Санкт-Петербург",
  "id" : 10,
  "to_time" : "20.08.2024 3:58",
  "from_time" : "19.08.2024 20:24"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Update an existing train route
 * Update an existing train route by Id
 *
 * body TrainRoute Update an existing train route
 * returns TrainRoute
 **/
exports.updateTrainRoute = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "cost" : 3700,
  "from_city" : "Тверь",
  "to_city" : "Санкт-Петербург",
  "id" : 10,
  "to_time" : "20.08.2024 3:58",
  "from_time" : "19.08.2024 20:24"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Update an existing train route
 * Update an existing train route by Id
 *
 * body TrainRoute Update an existing train route
 * returns TrainRoute
 **/
exports.updateTrainRoute = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "cost" : 3700,
  "from_city" : "Тверь",
  "to_city" : "Санкт-Петербург",
  "id" : 10,
  "to_time" : "20.08.2024 3:58",
  "from_time" : "19.08.2024 20:24"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

