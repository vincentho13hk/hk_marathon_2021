export interface Fetch {
  meta: Meta;
  eventRace: EventRace;
  fullClassifications?: FullClassificationsEntity[] | null;
}
export interface Meta {
  numberOfAthletes: number;
  numberOfEvents: number;
  numberOfClassifications: number;
  categories?: string[] | null;
  count: number;
  offset: number;
}
export interface EventRace {
  event: Event;
  race: Race;
}
export interface Event {
  id: string;
  countryCode: string;
  name: string;
  date: string;
  displayDate: string;
  city: string;
  activity: string;
  activityType: number;
  organization: string;
  lastUpdate: string;
  cmsId: number;
  themeMainColor: number;
  backgroundPhotoUrl: string;
  sponsorPhotoUrl: string;
  appLogoPhotoUrl: string;
  certificateFontName: string;
  certificateReportName: string;
  hideIndividualDetails: boolean;
  enableCertificate: boolean;
  enableTeamCertificate: boolean;
  showGenderOnOverview: boolean;
  showCountryOnOverview: boolean;
  unitSystem: number;
  useFinishTime: number;
  roundTime: number;
  autoCalculatePositions: number;
  config: Config;
  customContent: CustomContent;
  organizations?: OrganizationsEntity[] | null;
  eventMode: number;
  latitude: number;
  longitude: number;
  totalParticipants: number;
  hidden: boolean;
  source: number;
  lastUploadLogPhotos: LastUploadLogPhotosOrLastUploadLogVideos;
  lastUploadLogVideos: LastUploadLogPhotosOrLastUploadLogVideos;
}
export interface Config {
  athletePhotoUrlTemplate: string;
  allowResultsDownload: boolean;
  showCityOnOverview: boolean;
  showTeamsOnOverview: boolean;
  calculateSpeedCumilative: boolean;
  defaultCulture: string;
  showScoreOnOverview: boolean;
}
export interface CustomContent {}
export interface OrganizationsEntity {
  role: number;
  id: string;
  name: string;
  url: string;
  primaryColor: string;
  source: number;
}
export interface LastUploadLogPhotosOrLastUploadLogVideos {
  uploadResult: number;
}
export interface Race {
  id: string;
  version: string;
  importType: number;
  name: string;
  distanceInMeter: number;
  displayDistance: string;
  numberOfAthletes: number;
  date: string;
  displayDate: string;
  teams?: null[] | null;
  classificationsCount: number;
  teamsCount: number;
  lastUpdate: string;
  statistics: Statistics;
  prochipRaceType: number;
  order: number;
  config: Config1;
  uploadWarnings?: null[] | null;
  lastUploadLog: LastUploadLog;
}
export interface Statistics {
  hasOverallRankData: boolean;
  hasTeamData: boolean;
  hasTeamScore: boolean;
  hasTeamNetTime: boolean;
  hasTeamPosition: boolean;
  hasTeamLogo: boolean;
  showTeamResults: boolean;
  hasCategoryData: boolean;
  hasGuntimeData: boolean;
  hasChiptimeData: boolean;
  hasAwardData: boolean;
  hasScoreData: boolean;
  showGenderOnOverview: boolean;
  showCountryOnOverview: boolean;
  showCityOnOverview: boolean;
  showDownloadOption: boolean;
  categories?: string[] | null;
  customColumns?: string[] | null;
}
export interface Config1 {
  useFinishTime: number;
  sordOrder: number;
  certificateTemplate: string;
}
export interface LastUploadLog {
  lastUpdate: string;
  uploadResult: number;
}
export interface FullClassificationsEntity {
  athlete: Athlete;
  classification: Classification;
}
export interface Athlete {
  id: string;
  name: string;
  birthYear: number;
  numberOfClassifications: number;
}
export interface Classification {
  id: string;
  eventId: string;
  raceId: string;
  bib: string;
  bibForUrl: string;
  category: string;
  rank: number;
  genderRank: number;
  categoryRank: number;
  gunTime: string;
  chipTime: string;
  primaryDisplayTime: string;
  speedInKmh: number;
  name: string;
  activityType: number;
  gender: number;
  splits?: SplitsEntity[] | null;
  gunTimeInSec: number;
  chipTimeInSec: number;
  customValues?: string[] | null;
  displayDistance: string;
  qualified: boolean;
}
export interface SplitsEntity {
  distanceInMeter: number;
  cumulativeTime: string;
  speedInKmh: number;
  speedInKmhRaceAverage: number;
  name: string;
}
