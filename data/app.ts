import testJson from "./test.json";
import fetchCOnfigJson from "./fetch-config.json";
import axios from "axios";
import { Classification, Fetch, FullClassificationsEntity } from "./types";
import fs from "fs";

fetchCOnfigJson.race.forEach(async (race) => {
  let fetchTimes = Math.ceil(race.count / 15);
  let classificationData: Classification[] = [];
  for (let i = 0; i < fetchTimes; i++) {
    let { data } = await axios.get<Fetch>(
      `https://eventresults-api.sporthive.com/api/events/6842055555920915712/races/${
        race.id
      }/classifications/search?count=${50}&offset=${50 * i}`
    );
    data.fullClassifications?.forEach((fullClassification) => {
      classificationData.push(fullClassification.classification);
    });

    setTimeout(() => {}, 1000);
  }
  let dataJson = JSON.stringify({ classification: classificationData });
  fs.writeFile(`result(${race.name}).json`, dataJson, (err) => {
    // Error checking
    if (err) throw err;
    console.log(`${race.name} Completed`);
  });
});
