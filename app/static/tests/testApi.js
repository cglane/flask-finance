var should = require('should');
var assert = require('assert');
var supertest = require('supertest');
var url = 'http://localhost:5000/'
var request = supertest(url)
var testData = require('./testData.js')
var userId = ''
describe('Test me',function(){
  it('Should create user',function(done){
    request.post('api/user')
    .send(testData.user1)
    .end(function(err,res){
      if(err)throw err;
      console.log(res.body,'body');
      res.status.should.be.equal(200)
      done()
    })
  })
  it('Should login',function(done){
    request.post('api/login')
    .send(testData.user1)
    .end(function(err,res){
      if(err)throw err;
      userId = res.body._id
      res.status.should.be.equal(200)
      done()
    })
  })
  it('Should save finances profile as part of user',function(done){
    request.post('api/save_finances/'+userId)
    .send(testData.financesProfile)
    .end(function(err,res){
      if(err)throw err;
      console.log(res.body);
      res.status.should.be.equal(200)
      done()
    })
  })
  it('Should save amex profile and insert into user',function(done){
    request.post('api/save_amex/'+userId)
    .send(testData.amexProfile)
    .end(function(err,res){
      if(err)throw err;
      res.status.should.be.equal(200)
      done()
    })
  })
  it('Should be able to read finances file',function(done){
    request.get('api/read_user_profiles/'+userId+'/'+'finances')
    .end(function(err,res){
      if(err)throw err;
      res.status.should.be.equal(200)
      done()
    })
  })
  it('Should be able to read amex file',function(done){
    request.get('api/read_user_profiles/'+userId+'/'+'amex')
    .end(function(err,res){
      if(err)throw err;
      res.status.should.be.equal(200)
      done()
    })
  })
  it('Should describe transactions',function(done){
    request.post('api/describe_transactions/'+userId+'/'+'amex')
    .send({'outputName':testData.outputName})
    .end(function(err,res){
      if(err)throw err;
      res.status.should.be.equal(200)
      done()
    })
  })
})
