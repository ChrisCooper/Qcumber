//
//  SectionComponent.h
//  Qcumber
//
//  Created by Chris Cooper on 12-01-01.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class Timeslot;

@interface SectionComponent : NSManagedObject

@property (nonatomic, strong) NSDate * endDate;
@property (nonatomic, strong) NSString * instructor;
@property (nonatomic, strong) NSString * room;
@property (nonatomic, strong) NSDate * startDate;
@property (nonatomic, strong) Timeslot *timeslot;
@property (nonatomic, strong) NSManagedObject *section;

@end
