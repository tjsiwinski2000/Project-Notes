export function IsWeekend(d){
  let dateIn_Day;
  dateIn_Day=d.format('dddd');
  console.log (dateIn_Day);
  if ( (dateIn_Day === 'Saturday') || (dateIn_Day === 'Sunday' )){
    return true;
  } else {
    return false;
  }
}
export default IsWeekend;