function resolveAfter2Seconds() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('resolved');
    }, 2000);
  });
}

async function asyncCall() {
  console.log('calling');
  const result = await resolveAfter2Seconds();
  console.log(result);
  console.log("Finally Finished");
  // Expected output: "resolved"
}

const prom = new promise((resolve, reject) => {
  if(resolve) {
  return new Promise((resolve) => {
    resolve('I am Dave!')

    .then(() => {
      consolce.log('Called')
    });

    .then(() => {
      console.log('Another Called!')
    });
  });
});

prom(setTimeOut( ()=>{
  console.log('TimeOut Called!');
}, 2000 ));
