//
//  SectionComponent.h
//  Qcumber
//
//  Created by Chris Cooper on 11-10-19.
//  Copyright (c) 2011 Chris Cooper. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class Section, Timeslot;

@interface SectionComponent : NSManagedObject {
@private
}
@property (nonatomic, retain) NSString * end_date;
@property (nonatomic, retain) NSString * instructor;
@property (nonatomic, retain) NSString * room;
@property (nonatomic, retain) NSString * start_date;
@property (nonatomic, retain) Section *section;
@property (nonatomic, retain) Timeslot *timeslot;

@end
