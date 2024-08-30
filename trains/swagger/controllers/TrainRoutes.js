'use strict';

var utils = require('../utils/writer.js');
var TrainRoutes = require('../service/TrainRoutesService');

module.exports.addTrainRoute = function addTrainRoute (req, res, next, body) {
  TrainRoutes.addTrainRoute(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.addTrainRoute = function addTrainRoute (req, res, next, body) {
  TrainRoutes.addTrainRoute(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.deleteTrainRoute = function deleteTrainRoute (req, res, next, id) {
  TrainRoutes.deleteTrainRoute(id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getTrainRouteById = function getTrainRouteById (req, res, next, id) {
  TrainRoutes.getTrainRouteById(id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getTrainRoutes = function getTrainRoutes (req, res, next) {
  TrainRoutes.getTrainRoutes()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.updateTrainRoute = function updateTrainRoute (req, res, next, body) {
  TrainRoutes.updateTrainRoute(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.updateTrainRoute = function updateTrainRoute (req, res, next, body) {
  TrainRoutes.updateTrainRoute(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
