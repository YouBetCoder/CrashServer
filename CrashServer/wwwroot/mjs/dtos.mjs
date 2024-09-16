/* Options:
Date: 2024-09-16 13:44:23
Version: 8.40
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
export class AppUser {
    /** @param {{id?:string,firstName?:string,userName?:string,lastName?:string,displayName?:string}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {string} */
    id;
    /** @type {?string} */
    firstName;
    /** @type {?string} */
    userName;
    /** @type {?string} */
    lastName;
    /** @type {?string} */
    displayName;
}
export class ApplicationUserPaymentLog {
    /** @param {{id?:number,paymentCoversFrom?:string,paymentCoversUntil?:string,costUsd?:number,costSol?:number,usersId?:string,applicationAppUser?:AppUser,transactionHash?:string,notes?:string}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {number} */
    id;
    /** @type {string} */
    paymentCoversFrom;
    /** @type {string} */
    paymentCoversUntil;
    /** @type {number} */
    costUsd;
    /** @type {number} */
    costSol;
    /** @type {?string} */
    usersId;
    /** @type {AppUser} */
    applicationAppUser;
    /** @type {string} */
    transactionHash;
    /** @type {string} */
    notes;
}
export class ActiveGameRoom {
    /** @param {{id?:number,gameNumber?:number,roomId?:number,roundId?:number,gameStatus?:string,gamePhase?:string,gameResult?:number,noMoreBetsAt?:number,timeRecorded?:number}} [init] */
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
    /** @type {?number} */
    timeRecorded;
}
/** @typedef From {any} */
/** @typedef  Into {any} */
export class QueryDb_2 extends QueryBase {
    /** @param {{skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
}
export class ActiveGameResult {
    /** @param {{id?:number,gameNumber?:number,roomId?:number,activeGameRoomRoundId?:number,gameResult?:number,prediction?:number,prediction2?:number,prediction3?:number,prediction4?:number,predictionArima?:number,noMoreBetsAt?:number}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {number} */
    id;
    /** @type {number} */
    gameNumber;
    /** @type {number} */
    roomId;
    /** @type {number} */
    activeGameRoomRoundId;
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
    /** @type {number} */
    noMoreBetsAt;
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
export class NotifyLiveViewDataUpdatedResponse {
    constructor(init) { Object.assign(this, init) }
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
export class NotifyLiveViewDataUpdatedRequest {
    /** @param {{id?:number,teaCup?:boolean}} [init] */
    constructor(init) { Object.assign(this, init) }
    /** @type {number} */
    id;
    /** @type {boolean} */
    teaCup;
    getTypeName() { return 'NotifyLiveViewDataUpdatedRequest' }
    getMethod() { return 'POST' }
    createResponse() { return new NotifyLiveViewDataUpdatedResponse() }
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
export class ApiQueryActiveGameRoomPrediction extends QueryDb_1 {
    /** @param {{id?:number,skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
    /** @type {?number} */
    id;
    getTypeName() { return 'ApiQueryActiveGameRoomPrediction' }
    getMethod() { return 'GET' }
    createResponse() { return new QueryResponse() }
}
export class QueryActiveGameRoomPrediction extends QueryDb_1 {
    /** @param {{id?:number,roundId?:number,roundIds?:number[],skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
    /** @type {?number} */
    id;
    /** @type {?number} */
    roundId;
    /** @type {number[]} */
    roundIds;
    getTypeName() { return 'QueryActiveGameRoomPrediction' }
    getMethod() { return 'GET' }
    createResponse() { return new QueryResponse() }
}
export class QueryApplicationUserPaymentLog extends QueryDb_1 {
    /** @param {{id?:number,paymentCoversFrom?:string,paymentCoversUntil?:string,applicationUserId?:string,skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
    /** @type {?number} */
    id;
    /** @type {?string} */
    paymentCoversFrom;
    /** @type {?string} */
    paymentCoversUntil;
    /** @type {?string} */
    applicationUserId;
    getTypeName() { return 'QueryApplicationUserPaymentLog' }
    getMethod() { return 'GET' }
    createResponse() { return new QueryResponse() }
}
export class ApiQueryActiveGameRoom extends QueryDb_1 {
    /** @param {{id?:number,roundId?:number,roomId?:number,timeRecorded?:number,skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
    /** @type {?number} */
    id;
    /** @type {?number} */
    roundId;
    /** @type {?number} */
    roomId;
    /** @type {?number} */
    timeRecorded;
    getTypeName() { return 'ApiQueryActiveGameRoom' }
    getMethod() { return 'GET' }
    createResponse() { return new QueryResponse() }
}
export class QueryActiveGameRoom extends QueryDb_1 {
    /** @param {{id?:number,roundId?:number,roomId?:number,timeRecorded?:number,skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
    /** @type {?number} */
    id;
    /** @type {?number} */
    roundId;
    /** @type {?number} */
    roomId;
    /** @type {?number} */
    timeRecorded;
    getTypeName() { return 'QueryActiveGameRoom' }
    getMethod() { return 'GET' }
    createResponse() { return new QueryResponse() }
}
export class ApiQueryActiveRoomPredictionResults extends QueryDb_2 {
    /** @param {{skip?:number,take?:number,orderBy?:string,orderByDesc?:string,include?:string,fields?:string,meta?:{ [index: string]: string; }}} [init] */
    constructor(init) { super(init); Object.assign(this, init) }
    getTypeName() { return 'ApiQueryActiveRoomPredictionResults' }
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
export class CreateApplicationUserPaymentLog {
    constructor(init) { Object.assign(this, init) }
    getTypeName() { return 'CreateApplicationUserPaymentLog' }
    getMethod() { return 'POST' }
    createResponse() { return new IdResponse() }
}
export class CreateActiveGameRoom {
    /** @param {{gameNumber?:number,roomId?:number,roundId?:number,gameStatus?:string,gamePhase?:string,gameResult?:number,noMoreBetsAt?:number,timeRecorded?:number}} [init] */
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
    /** @type {number} */
    timeRecorded;
    getTypeName() { return 'CreateActiveGameRoom' }
    getMethod() { return 'POST' }
    createResponse() { return new IdResponse() }
}

