/* Options:
Date: 2024-09-09 10:38:43
Version: 8.30
Tip: To override a DTO option, remove "//" prefix before updating
BaseUrl: https://localhost:5001

//AddServiceStackTypes: True
//AddDocAnnotations: True
//AddDescriptionAsComments: True
//IncludeTypes: 
//ExcludeTypes: 
//DefaultImports: 
*/

"use strict";
export class QueryBase {
    /** @param {{skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {?number} */
    skip;
    /** @type {?number} */
    take;
    /** @type {string} */
    orderBy;
    /** @type {string} */
    orderByDesc;
    /** @type {string} */
    include;
    /** @type {string} */
    fields;
    /** @type {{ [index: string]: string; }} */
    meta;
}
/** @typedef T {any} */
export class QueryDb_1 extends QueryBase {
    /** @param {{skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
}
export class ActiveGameRoomPrediction {
    /** @param {{id?:number,gameNumber?:number,roomId?:number,activeGameRoomId?:number,roundId?:number,prediction?:number,prediction2?:number,prediction3?:number,prediction4?:number,predictionArima?:number}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {number} */
    id;
    /** @type {number} */
    gameNumber;
    /** @type {number} */
    roomId;
    /** @type {?number} */
    activeGameRoomId;
    /** @type {number} */
    roundId;
    /** @type {number} */
    prediction;
    /** @type {number} */
    prediction2;
    /** @type {number} */
    prediction3;
    /** @type {number} */
    prediction4;
    /** @type {number} */
    predictionArima;
}
export class ActiveGameRoom {
    /** @param {{id?:number,gameNumber?:number,roomId?:number,roundId?:number,gameStatus?:string,gamePhase?:string,gameResult?:number,noMoreBetsAt?:number}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {number} */
    id;
    /** @type {number} */
    gameNumber;
    /** @type {number} */
    roomId;
    /** @type {number} */
    roundId;
    /** @type {string} */
    gameStatus;
    /** @type {string} */
    gamePhase;
    /** @type {number} */
    gameResult;
    /** @type {number} */
    noMoreBetsAt;
}
/** @typedef From {any} */
/** @typedef  Into {any} */
export class QueryDb_2 extends QueryBase {
    /** @param {{skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
}
export class ActiveGameResult {
    /** @param {{activeGameResultGameNumber?:number,activeGameResultRoomId?:number,activeGameResultRoundId?:number,gameResult?:number,prediction?:number,prediction2?:number,prediction3?:number,prediction4?:number,predictionArima?:number}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {number} */
    activeGameResultGameNumber;
    /** @type {number} */
    activeGameResultRoomId;
    /** @type {number} */
    activeGameResultRoundId;
    /** @type {number} */
    gameResult;
    /** @type {number} */
    prediction;
    /** @type {number} */
    prediction2;
    /** @type {number} */
    prediction3;
    /** @type {number} */
    prediction4;
    /** @type {number} */
    predictionArima;
}
export class ResponseError {
    /** @param {{errorCode?:string,fieldName?:string,message?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {string} */
    errorCode;
    /** @type {string} */
    fieldName;
    /** @type {string} */
    message;
    /** @type {{ [index: string]: string; }} */
    meta;
}
export class ResponseStatus {
    /** @param {{errorCode?:string,message?:string,stackTrace?:string,errors?:ResponseError[],meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {string} */
    errorCode;
    /** @type {string} */
    message;
    /** @type {string} */
    stackTrace;
    /** @type {ResponseError[]} */
    errors;
    /** @type {{ [index: string]: string; }} */
    meta;
}
export class HelloResponse {
    /** @param {{result?:string}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {string} */
    result;
}
export class AuthenticateResponse {
    /** @param {{userId?:string,sessionId?:string,userName?:string,displayName?:string,referrerUrl?:string,bearerToken?:string,refreshToken?:string,refreshTokenExpiry?:string,profileUrl?:string,roles?:string[],permissions?:string[],responseStatus?:ResponseStatus,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {string} */
    userId;
    /** @type {string} */
    sessionId;
    /** @type {string} */
    userName;
    /** @type {string} */
    displayName;
    /** @type {string} */
    referrerUrl;
    /** @type {string} */
    bearerToken;
    /** @type {string} */
    refreshToken;
    /** @type {?string} */
    refreshTokenExpiry;
    /** @type {string} */
    profileUrl;
    /** @type {string[]} */
    roles;
    /** @type {string[]} */
    permissions;
    /** @type {ResponseStatus} */
    responseStatus;
    /** @type {{ [index: string]: string; }} */
    meta;
}
/** @typedef T {any} */
export class QueryResponse {
    /** @param {{offset?:number,total?:number,results?:T[],meta?:{ [index: string]: string; },responseStatus?:ResponseStatus}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {number} */
    offset;
    /** @type {number} */
    total;
    /** @type {T[]} */
    results;
    /** @type {{ [index: string]: string; }} */
    meta;
    /** @type {ResponseStatus} */
    responseStatus;
}
export class IdResponse {
    /** @param {{id?:string,responseStatus?:ResponseStatus}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {string} */
    id;
    /** @type {ResponseStatus} */
    responseStatus;
}
export class Hello {
    /** @param {{name?:string}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {?string} */
    name;
    getTypeName() { return 'Hello' }
    getMethod() { return 'POST' }
    createResponse() { return new HelloResponse() }
}
export class Authenticate {
    /** @param {{provider?:string,userName?:string,password?:string,rememberMe?:boolean,accessToken?:string,accessTokenSecret?:string,returnUrl?:string,errorView?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { Object.assign(this, init) }
    /**
     * @type {string}
     * @description AuthProvider, e.g. credentials */
    provider;
    /** @type {string} */
    userName;
    /** @type {string} */
    password;
    /** @type {?boolean} */
    rememberMe;
    /** @type {string} */
    accessToken;
    /** @type {string} */
    accessTokenSecret;
    /** @type {string} */
    returnUrl;
    /** @type {string} */
    errorView;
    /** @type {{ [index: string]: string; }} */
    meta;
    getTypeName() { return 'Authenticate' }
    getMethod() { return 'POST' }
    createResponse() { return new AuthenticateResponse() }
}
export class QueryActiveGameRoomPrediction extends QueryDb_1 {
    /** @param {{id?:number,skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
    /** @type {?number} */
    id;
    getTypeName() { return 'QueryActiveGameRoomPrediction' }
    getMethod() { return 'GET' }
    createResponse() { return new QueryResponse() }
}
export class QueryActiveGameRoom extends QueryDb_1 {
    /** @param {{id?:number,roundId?:number,skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
    /** @type {?number} */
    id;
    /** @type {?number} */
    roundId;
    getTypeName() { return 'QueryActiveGameRoom' }
    getMethod() { return 'GET' }
    createResponse() { return new QueryResponse() }
}
export class QueryActiveRoomPredictionResults extends QueryDb_2 {
    /** @param {{skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
    getTypeName() { return 'QueryActiveRoomPredictionResults' }
    getMethod() { return 'GET' }
    createResponse() { return new QueryResponse() }
}
export class CreateActiveGameRoomPrediction {
    /** @param {{gameNumber?:number,roomId?:number,roundId?:number,prediction?:number,prediction2?:number,prediction3?:number,prediction4?:number,predictionArima?:number,activeGameRoomId?:number}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {number} */
    gameNumber;
    /** @type {number} */
    roomId;
    /** @type {number} */
    roundId;
    /** @type {number} */
    prediction;
    /** @type {number} */
    prediction2;
    /** @type {number} */
    prediction3;
    /** @type {number} */
    prediction4;
    /** @type {number} */
    predictionArima;
    /** @type {?number} */
    activeGameRoomId;
    getTypeName() { return 'CreateActiveGameRoomPrediction' }
    getMethod() { return 'POST' }
    createResponse() { return new IdResponse() }
}
export class CreateActiveGameRoom {
    /** @param {{gameNumber?:number,roomId?:number,roundId?:number,gameStatus?:string,gamePhase?:string,gameResult?:number,noMoreBetsAt?:number}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {number} */
    gameNumber;
    /** @type {number} */
    roomId;
    /** @type {number} */
    roundId;
    /** @type {string} */
    gameStatus;
    /** @type {string} */
    gamePhase;
    /** @type {number} */
    gameResult;
    /** @type {number} */
    noMoreBetsAt;
    getTypeName() { return 'CreateActiveGameRoom' }
    getMethod() { return 'POST' }
    createResponse() { return new IdResponse() }
}

